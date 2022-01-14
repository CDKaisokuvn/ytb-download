import typer
from rich.table import Table
from rich.console import Console
from tooldload import download_playlist, download_single

console = Console()

app = typer.Typer()


@app.command(short_help='Playlist url to download and destination folder')
def list(url: str, destination: str):
    typer.echo(f"download from {url} to {destination}")
    download_playlist(url, destination)


@app.command(short_help="Url of video to download and destination folder")
def single(url: str, destination: str):
    typer.echo(f"download from {url} to {destination}")
    download_single(url, destination)


if __name__ == "__main__":
    app()