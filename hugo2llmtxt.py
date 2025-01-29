
import typer
import csv
from collections import defaultdict
app = typer.Typer()

def output(sections: list[str], output_path: str):
    with open(output_path, mode='w') as f:
        count = 0
        for section, titles in sections.items():
            f.write(f"# {section}\n")
            for title in titles:
                f.write(f"- {title}\n")
                count += 1
        typer.echo(f"Output written to {output_path}. Total links: {count}")

@app.command()
def llm2txt(file_path: str = typer.Argument(..., help="Path to the CSV file obtained by running `hugo list all > hugo_list.all.csv`"),
            ouput_path: str = typer.Argument(..., help="Path to the output text file like `static/llms.txt`")):
    sections = defaultdict(list)
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row.get('title', 'N/A')
                permalink = row.get('permalink', 'N/A')
                # If the section is empty string not None
                section = row.get('section', 'Misc') or 'Misc'
                if  title:
                    sections[section].append(f"[{title}]({permalink}): {title}")
            output(sections, ouput_path)
    except FileNotFoundError:
        typer.echo(f"File not found: {file_path}")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")


if __name__ == "__main__":
    app()