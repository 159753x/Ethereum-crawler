# Ethereum Crawler

This Python application crawls Ethereum data using the Etherscan API. It allows you to interact with Ethereum blockchain data through a simple console output.

## Quick Start

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/ethereum-crawler.git
cd ethereum-crawler
```

### 2. Install Dependencies

Ensure you have Python 3.7+ installed. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up `.env` File

You need to create a `.env` file to securely store your **Etherscan API key**.

- Copy the provided `example.env` file:

```bash
cp example.env .env
```

- Open the `.env` file in a text editor and replace the placeholder `<YOUR_ETHERSCAN_API_KEY>` with your actual Etherscan API key.

### 4. Obtain Etherscan API Key

To obtain your **Etherscan API key**, follow these steps:

1. Go to the [Etherscan API](https://etherscan.io/apis) page.
2. Sign up or log in to your Etherscan account.
3. Navigate to **API Keys** and click **Create New API Key**.
4. Copy the generated key and paste it into your `.env` file under the `ETHERSCAN_API_KEY` variable.

### 5. Run the Application

After setting up the `.env` file, you can start the crawler by running the following command:

```bash
python app.py
```

The app will start, and you’ll see the console output as it interacts with the Ethereum network through the Etherscan API.

## Example Output

```bash
Fetching data from Ethereum blockchain...
Transaction found: 0x123456789abcdef...
Balance: 5 ETH
Block Number: 1234567
...
```

## Additional Notes

- Ensure your `.env` file is **not committed to version control**. You can add `.env` to your `.gitignore` file to prevent accidental commits.
- You can refer to the [Etherscan API documentation](https://etherscan.io/apis) for more details on available API endpoints and parameters.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
