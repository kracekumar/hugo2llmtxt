A simple utility to generate [llms.txt](https://llmstxt.org/) for hugo website.

### Run

- Make sure to run `hugo list all > hugo_list.csv` that contains all the contents in the CSV file.
- `uvx --from hugo2llmtxt hugo2llmtxt ../hugo_list.csv  ../static/llms.txt`
- The command should generate the llms.txt


