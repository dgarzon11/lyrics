# Song Lyrics Finder

A simple and interactive web application built with Streamlit that allows users to find the lyrics of their favorite songs. This app uses the `lyricsgenius` library to fetch song lyrics from Genius.

## Features

- **Search by Artist and Song**: Users can enter the name of an artist and a song to find its lyrics.
- **Clean Lyrics Display**: The application processes the fetched lyrics to remove unnecessary text, providing a clean and readable output.

## How to Run Locally

### Prerequisites

- Python 3
- Streamlit
- LyricsGenius API Token

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/song-lyrics-finder.git
```

2. Install the required libraries:
```bash
pip install streamlit lyricsgenius
```

3. Set up your Genius API token. You can obtain a token from [Genius API](https://docs.genius.com/).

4. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

After running the app, input the artist's name and song title in the respective fields. The lyrics will be displayed if they are found.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



