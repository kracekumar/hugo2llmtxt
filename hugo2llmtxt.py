
import typer
import sys
import csv
from collections import defaultdict
app = typer.Typer()

def output(sections: dict[str, list[dict[str, str]]], output_path: str, render_content: bool=False):
    with open(output_path, mode='w') as f:
        count = 0
        for section, articles in sections.items():
            f.write(f"# {section}\n")
            for article in articles:
                f.write(f"- {article['title']}\n")
                if render_content:
                    f.write(article['content'])
                    f.write('\n')
                count += 1
        typer.echo(f"Output written to {output_path}. Total links: {count}")

@app.command()
def llm2txt(file_path: str = typer.Argument(..., help="Path to the CSV file obtained by running `hugo list all > hugo_list.all.csv`"),
            ouput_path: str = typer.Argument(..., help="Path to the output text file like `static/llms.txt`"),
            render_content: bool = typer.Argument(..., help="Whether to output entire blog content to a file. Pass true for `llms-full.txt`")):
    sections = defaultdict(list[dict[str, str]])
    # sections = {'page': [{'title': 'hello world', 'content': 'This is hollow world'}]}
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row.get('title', 'N/A')
                permalink = row.get('permalink', 'N/A')
                # If the section is empty string not None
                section = row.get('section', 'Misc') or 'Misc'
                if  title:
                    item = {}
                    item['title'] = f"[{title}]({permalink}index.md): {title}"
                    try:
                        item['content'] = open(row['path']).read()
                    except FileNotFoundError:
                        typer.echo(f"File not found: {row['path']}", err=True)
                        sys.exit(-1)
                    sections[section].append(item)
            output(sections, ouput_path, render_content)
    except FileNotFoundError:
        typer.echo(f"File not found: {file_path}", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
