from google import genai
import argparse


def main(args):
  # Initialize LLM client with api key
  client = genai.Client(api_key=args.api_key)

  with open(args.input, 'r') as f:
    # Get raw CSV text
    data = f.read()

  # Changes how LLM interacts with data
  prompt = "Treating this data as a csv, respond to the question under column B. Return in csv format with the answer in the same column in a new row. Do not format with markdown"
  response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=[data, prompt],
  )
  
  with open("output.csv", 'w') as f:
    # Write to output
    f.write(response.text)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--input","-i")
  parser.add_argument("--api_key")
  args = parser.parse_args()
  main(args)