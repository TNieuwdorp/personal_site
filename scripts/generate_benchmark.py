import polars as pl
from plotnine import *
from plotnine import position_dodge

data = [
    ("pip", 154.276, "Cold Install"),
    ("poetry", 53.169, "Cold Install"),
    ("uv", 5.908, "Cold Install"),
    ("pip", 102.244, "Warm Install"),
    ("poetry", 20.641, "Warm Install"),
    ("uv", 0.029, "Warm Install"),
]
df = pl.DataFrame(
    data,
    schema=["Tool", "Time", "InstallType"],
    orient="row",
).with_columns(pl.col("InstallType").cast(pl.Categorical))

plot = (
    ggplot(df, aes(x="InstallType", y="Time", fill="Tool"))
    + geom_col(
        position=position_dodge(width=0.7),
        width=0.6,
        color="white",
        size=0.5,
        alpha=0.9,
    )
    + coord_flip()
    + labs(
        title="Package Manager Performance Comparison",
        x="Install Type",
        y="Time (seconds)",
        fill="Package Manager",
    )
    + scale_fill_manual(values={"pip": "#FF6F42", "uv": "#42A5F5", "poetry": "#FF0000"})
    + scale_x_discrete(
        limits=["Warm Install", "Cold Install"],
        labels=["Warm Install", "Cold Install"],
    )
    + theme_dark()
    + theme(
        text=element_text(color="white"),
        panel_background=element_rect(fill="#1a1a1a"),
        plot_background=element_rect(fill="#1a1a1a"),
        legend_background=element_rect(fill="#1a1a1a"),
        legend_position="top",
        axis_title_y=element_text(margin={"r": 15}),
        axis_title_x=element_text(margin={"t": 10}),
        panel_grid_major_x=element_line(color="#333333"),
        panel_grid_minor_x=element_blank(),
        plot_title=element_text(size=14, ha="center", margin={"b": 15}),
    )
    + geom_segment(
        df.filter(
            (pl.col("Tool") == "uv") & (pl.col("InstallType") == "Warm Install")
        ).to_pandas(),
        aes(x=1.38, xend=1.38, y=0, yend=0.029),
        color="#42A5F5",
        size=1.5,
        inherit_aes=False,
    )
)

plot.save("static/images/benchmark.png", dpi=300)
