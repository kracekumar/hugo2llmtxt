A simple utility to generate [llms.txt](https://llmstxt.org/) for hugo website.

### Usage

```
hugo2llmtxt --help
Usage: hugo2llmtxt.py [OPTIONS] FILE_PATH OUPUT_PATH RENDER_CONTENT

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    file_path           TEXT  Path to the CSV file obtained by running `hugo list all > hugo_list.all.csv` [default: None] [required]             │
│ *    ouput_path          TEXT  Path to the output text file like `static/llms.txt` [default: None] [required]                                      │
│ *    render_content            Whether to output entire blog content to entire file. Pass true for `llmsfull.txt` [default: None] [required]       │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```
### Run

- Make sure to run `hugo list all > hugo_list.csv` that contains all the contents in the CSV file.
- `uvx --from hugo2llmtxt hugo2llmtxt hugo_list.csv  static/llms.txt false` to generate the llms.txt file.
- `uvx --from hugo2llmtxt hugo2llmtxt hugo_list.csv  static/llms-full.txt false`
- These command should generate the llms.txt and llm-full.txt files.
