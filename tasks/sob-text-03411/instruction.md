Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Auctiva: Auctiva is an eBay auction management system that was founded in 1998.  One of the original members of the eBay Developer Council, Auctiva has provided sellers and merchants with tools designed to help increase their sales volume on eBay.  Jeff Schlicht, who founded Auctiva, wrote a program to automate the task of placing listings on eBay.  After giving the software to friends and family who enjoyed the convenience it provided, he formed Auctiva, which is used by individuals and businesses attempting to conduct e-commerce through eBay.

Pierre Omidyar: Pierre Morad Omidyar (Persian: پیر مراد امیدیار‎ ‎ , ] born June 21, 1967) is a French-American entrepreneur and philanthropist.  He is the founder of the eBay auction site where he served as chairman from 1998 to 2015.  He became a billionaire at the age of 31 with eBay's 1998 initial public offering (IPO).  Omidyar and his wife Pamela are well-known philanthropists who founded Omidyar Network in 2004 in order to expand their efforts beyond non-profits to include for-profits and public policy.

IBazar: iBazar is a free classifieds website which allows people to buy, sell, or trade services or products locally in Mexico.  Launched by eBay in April 2013, iBazar aims to provide a free online classifieds network for the Mexican population.  eBay acquired in early 2000's the French classifieds website iBazar before replacing it with eBay France but owning the name from then.  iBazar's name is also derived from bazaar to reflect Mexico's strong traditions of bazaars, flea markets, and fairs.

EBay: eBay Inc. ( , stylized as ebay) is a multinational e-commerce corporation, facilitating online consumer-to-consumer and business-to-consumer sales.  It is headquartered in San Jose, California.  eBay was founded by Pierre Omidyar in 1995, and became a notable success story of the dot-com bubble.  Today it is a multibillion-dollar business with operations in about 30 countries.

Brad Handler: Brad Handler (born July 19, 1967) is an American entrepreneur and attorney best known for his success in the destination club industry and his role as the first in-house attorney at eBay .  He is a founder and chairman of Inspirato, a private, luxury destination club.  In 2002, along with his brother Brent Handler, he founded Exclusive Resorts, where he served as chairman, CEO and vice-chairman.  He served as eBay's in-house attorney from 1997 to 2001.  He is based in Palo Alto, California.

List of acquisitions by eBay: eBay is an online auction website launched on September 3, 1995.  Each acquisition is for the respective company in its entirety, unless otherwise specified.  The acquisition date listed is the date of the agreement between eBay and the subject of the acquisition.  The value of each acquisition is listed in United States dollars because eBay is headquartered in the United States.  If the value of an acquisition is not listed, then it is undisclosed.

Blues to the Bush: Blues to the Bush is a live album by The Who recorded at the House of Blues in Chicago on 12 and 13 November 1999, and at the Empire Theatre, Shepherd's Bush on 22 and 23 December 1999.  It was sold exclusively from the now defunct MusicMaker.com, though it can still be found on torrent sites and second hand markets such as EBay.

MissionFish: Founded in 1999, MissionFish is the partner charity of eBay, which runs auction and shopping websites in 30 countries.  Through MissionFish, eBay users are able to donate to registered nonprofit organisations when they buy and sell through the eBay.com and eBay.co.uk sites.  The programmes are called eBay Giving Works and eBay for Charity, respectively.

Billpoint: Billpoint was the name of a person-to-person money transfer service founded in 1998 and purchased in 1999 by online auctioneer eBay.  It was founded by S Young Lee, Hope Chen, Will Chen, Jason May, Ian Flint and Jay Shen.  It obtained venture funding from Sequoia Capital in February 1999.  Billpoint's website was taken offline while eBay integrated Billpoint into its auction service, and it did not reappear until 2000, when it was relaunched as a joint venture with Wells Fargo bank.

Hobby Markets Online: Hobby Markets Online was an early internet auction company and which ran a series of person-to-person marketplaces for high-end collectibles.  The Company is cited as the second person-to-person online auction marketplace after eBay and launched its first web-based auction on October 15, 1995, several weeks after eBay had launched its first auction on September 12, 1995.  Both of these auction websites were launched in the San Francisco Bay Area although the respective founders did not know about each other or their websites at the time.

Question: You can buy Blues to the Bush on ebay. Who founded ebay in 1995?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "founder_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the founder."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in founding the company."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "founding_information": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the company was founded."
        },
        "headquarters_location": {
          "type": "string",
          "description": "The location of the company's headquarters."
        }
      },
      "required": [
        "year",
        "headquarters_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "founder_details",
    "founding_information"
  ],
  "additionalProperties": false
}
