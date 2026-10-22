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
Kenya Airways: Kenya Airways Ltd., more commonly known as Kenya Airways, is the flag carrier of Kenya.  The company was founded in 1977, after the dissolution of East African Airways.  The carrier's head office is located in Embakasi, Nairobi, with its hub at Jomo Kenyatta International Airport.

Wanjiku Mugane: Caroline Wanjiku Mugane is an attorney and investment banker in Kenya, the largest economy in the East African Community.  She is the Managing Director of "Fedha Connect Limited", a company that raises capital for businesses in agribusiness, real estate, oil and gas.  She is a member of the Board of Directors of Kenya Airways, the national airline.  She has previously served on the boards of Equity Bank, East African Breweries, and Standard Securities Limited.

East African Court of Justice: The East African Court of Justice (EACJ) is a treaty-based judicial body of the East African Community tasked to ensure adherence to law in the interpretation and application of and compliance with the East African Community Treaty of 1999.  The Court is made up of two divisions: a First Instance Division and an Appellate Division.  Its Judges, a maximum of ten in the First Instance Division and of five in the Appellate Division, are appointed by the East African Community Summit, the highest organ of the community, from among persons recommended by the Partner States who are of proven integrity, impartiality and independence and fulfill the conditions required in their own countries for high judicial office, or are jurists of recognised competence.

Irene Koki Mutungi: Airline Captain Irene Koki Mutungi, commonly known as Koki Mutungi, is a professional pilot in Kenya, the largest economy in the East African Community.  She was the first female on the African continent to become certified as a Captain of the Boeing 787 "Dreamliner" aircraft.  She flies for Kenya Airways, the national airline of Kenya.

Tanzanian shilling: "For earlier currencies used in Tanzania, see East African florin, East African rupee, East African shilling, Zanzibari rupee, Zanzibari ryal and German East African rupie."

Kenya Airways destinations: Kenya Airways was established by the Government of Kenya on 22 January 1977, following the collapse of the East African Union and the consequent folding of East African Airways.  It first flew on 4 February 1977 servicing the London–Nairobi route, using a Boeing 707–321 leased from British Midland Airways.  A year later, the airline's network comprised five domestic and 16 international destinations.  As of  1980 (1980-) , the airline served the international destinations of Addis Ababa, Athens, Bombay, Cairo, Copenhagen, Frankfurt, Jeddah, Kampala, Karachi, Khartoum, London, Lusaka, Mauritius, Mogadishu, Rome, Salisbury, Seychelles and Zurich and Kenyan cities (Kisumu, Malindi, Mombasa and Mumias).

Gina Din: Gina Din (born 23 October 1961) is a businesswoman in East Africa, particularly Kenya, specializing in strategic communication and public relations.  She worked at Barclays Bank for 14 years.  Some of her clients are Safaricom, Kenya Airways, KCB and Kenya Red Cross.  Din was born in Nanyuki, Kenya.  and attended the London School of Journalism.  She was named by the "New African" magazine as one of "100 Most Influential Africans" in business.  Gina is married to Christopher Kariuki and they have 2 children, Naytalya Din-Kariuki and Naythan Din-Kariuki.

East African Professional Hunter's Association: The East African Professional Hunter's Association (EAPHA) was an organization of East African white hunters founded in Nairobi, Kenya in 1934.  Well known members included Philip Percival, Harry Selby, Sydney Downey and Donald Ker.  Their motto was "nec timor nec temeritas", or "neither fear nor foolhardiness".  The Association formed out of a desire to regulate hunting in the wake of technological developments like the safari vehicle, which had made accessing remote hunting areas much easier.  During its existence it was able to accomplish much to conserve East African wildlife and become perhaps one of the most respected societies in the world of its kind.  The Association was disbanded in 1977 when Kenya outlawed all big game hunting.

Dudu Myeni: Duduzile Cynthia Myeni (born 29 October 1963), also known as "Dudu", is a South African businesswoman, the chairperson of South African Airways SOC Limited since January 2015, and the Executive Chairperson of the Jacob G Zuma Foundation since September 2008.  She is known for her controversial involvement with South African Airways and as a close friend of South African president Jacob Zuma.

East African Safari Air: East African Safari Air is an airline based in Kenya.  Its international operations were suspended in September 2004, by the Kenya Civil Aviation Authority, but the airline still maintained scheduled regional and domestic services through its subsidiary East African Safari Air Express.  In December 2010, East African Safari Air Express was ostensibly purchased by the parent company of another Kenyan airline Fly540 and was rebranded as Fly SAX.  (Litigation concerning this purchase is pending in Kenyan courts).

Question: which flag-carrying national airline, founded in 1977, is a client of the East African businesswoman Gina Din?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the national airline."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the airline was founded."
        },
        "is_flag_carrier": {
          "type": "boolean",
          "description": "Indicates if the airline is a flag carrier."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country the airline is from."
        }
      },
      "required": [
        "name",
        "founding_year",
        "is_flag_carrier",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "businesswoman_client_relationship": {
      "type": "object",
      "properties": {
        "businesswoman_name": {
          "type": "string",
          "description": "The name of the businesswoman."
        },
        "is_client": {
          "type": "boolean",
          "description": "True if the airline is a client of the businesswoman."
        }
      },
      "required": [
        "businesswoman_name",
        "is_client"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the airline that matches all criteria."
    }
  },
  "required": [
    "airline_details",
    "businesswoman_client_relationship",
    "final_answer"
  ],
  "additionalProperties": false
}
