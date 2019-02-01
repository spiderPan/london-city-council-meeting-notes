# Word Counter

Use [NLKT](https://www.nltk.org/) to do text mining within
[City of London Council and Committee Meetings Minutes in 2018](https://pub-london.escribemeetings.com/MeetingsContent?MeetingViewId=1)

## Getting Started


### Prerequisites

What things you need to install the software and how to install them
1. Python 3.*
2. Pip

### Installing

1. Clone the repo
    ```
    git clone git@github.com:spiderPan/london-city-council-meeting-notes.git
    ```
2. Install requirements packages within the repo
    ```
    cd london-city-council-meeting-notes
    pip install -r requirments.txt
    ```

## Running the tests
1. Download example meeting minutes from [Past Meetings](https://pub-london.escribemeetings.com/MeetingsContent?MeetingViewId=1&Expanded=Council)

2. Only grab the content part and put into the /data/html/ folder. The content part will starts with
    ```
    <main class="container body-content" style="background-color:#ffffff">
    ```        
3. Converting .html versions to .txt
    ```bash
    python html2txt.py
    ```
4. Run the counter
    ```bash
    python word_counter.py
    ```
5. Counter results will be found in the new `results.txt` file.

## Future Plan
The project can be improved by the following fields

1. Build a web crawler to fetching all meetings.
2. When converting HTML to txt, should merging multi HTML files into one.
3. Dockerlize the project so that no need to install nlkt local.
4. Future anlytises the text mining, and do data visualization.