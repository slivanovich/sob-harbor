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
Discovery Mine: The Discovery Mine was a gold mine 81 kilometers northeast (approx bearing of 15 degrees) of Yellowknife, Northwest Territories that operated between 1950 and 1969.  Gold was discovered here by Alfred Giauque in 1944.  A complete townsite, on Giauque Lake, was established by the company to house workers and their families.  The mine produced one million troy ounces (31,000 kg) of gold from one million tons of ore.  The abandoned townsite, not accessible by road, was demolished in 2005.

Northland Pyrite Mine: The Northland Pyrite Mine, also known as James Lake Mine, Rib Lake Mine, Harris Mine or simply Northland Mine, is an abandoned underground mine in Northeastern Ontario, Canada, located on the southwestern shore of James Lake in Best Township of Temagami.  It was operated by the Northland Mining Company during the early 1900s with the construction of a 91 m shaft and many open-cuts north of the shaft.  Minerals present at the mine include chalcopyrite, pyrite and pyrrhotite, deposited in Precambrian volcanic rock of the Canadian Shield.

Camlaren Mine: The Camlaren Mine was a small gold mine 80 km north-east of Yellowknife, Northwest Territories, Canada at Gordon Lake.  It consists of a property totaling about 981 hectares.  The two claims that make up the property were staked in 1936 by prospectors Don Cameron and the Mclaren brothers and developed with two shafts during 1937-1938.  The name "Camlaren" is a portmanteau of Cameron and McLaren.  Conditions attributed to World War II halted development at Camlaren in 1939.

Ruth Mine: The Ruth Mine was a small gold producer about 65 km (40 miles) east of Yellowknife, Northwest Territories.  It operated briefly during 1942 and then again in 1959, extracting only 550 troy ounces (17 kg) of gold thus far.  The old mine is today (2012) significant as one of the last intact abandoned mining properties from the 1940s period in the Northwest Territories, although the site was scheduled to be remediated by the federal government.

Burwash Mine: The Burwash Mine was a small gold property discovered in the fall of 1934 by Johnny Baker and Hugh Muir at Yellowknife Bay, Northwest Territories.  The town of Yellowknife did not exist yet at that point, but the discovery of gold at Burwash was the catalyst that brought more gold prospectors into the region in 1935 and 1936.  A short shaft was sunk in 1935-1936 at Burwash, and in the summer of 1935 a 16-ton bulk sample of ore was shipped to Trail, British Columbia for processing, yielding 200 troy ounces (6 kg) of gold.  The mine did not become a substantial producer and it is believed the gold vein was mined out.

Con Mine: The Con Mine (1938-2003) was the first gold mine developed in the Northwest Territories, Canada, just south of Yellowknife.  The property was staked by Consolidated Mining and Smelting Company of Canada (Cominco) in September 1935 in response to the discovery of visible gold nearby; the name "Con" is an abbreviation of "Consolidated".  The advent of winter prevented any prospecting from being conducted, but work in the summer of 1936 led to the discovery of numerous gold veins.  The Con Mine entered production in 1938 and ceased operations in 2003.  It has produced over 5000000 ozt of gold from 12,195,585 tons of ore processed.  The mine was over 6000 ft deep.

Løkken Mine: The Løkken Mine is and underground pyrite mine located in the municipality of Meldal in Sør-Trøndelag, Norway.  The mine was operative from 1654 to 1987, from the mining community Løkken Verk.  It contained the largest deposits of its kind in Norway.  Between 1654 and 1845, a total of 11,300 tons of copper was produced from the mine.  From 1904 the mine was run by the company Orkla Grube-Aktiebolag, and until 1987 a total of 24 million tons of pyrite was produced from the mine.  In addition to sulphur, the pyrite contained about 2% copper, in addition to zinc and traces of silver and gold.  The products were originally transported to the sea by horse and sledge during winter time.  From 1908 the ore was transported by the Thamshavn Line, which was the first electrical railway line in Norway.  The annual production was about 350,000 tons of ore during its final years.

Colomac Mine: The Colomac Mine was a privately owned and operated open pit gold mine located 220 km northwest of Yellowknife in the Northwest Territories in Canada .  The Colomac mine operated between 1990–1992, and 1994–1997.  It was operated by Neptune Resources Limited that had little success in making a profit during its operation.  In 1994, the mine had reopened under Royal Oak Mines Inc.  Both Neptune Resources and Royal Oak Mines where both owned and operated by Peggy Witte.  Due to low gold prices and high cost of mining, Royal Oak Mines was forced into bankruptcy.  The Federal Government of Canada became owners of the mine, along with the related environmental issues.  A major cleanup effort is under way to prevent the mine from polluting the environment, but this might be too late at this stage.  This mine is now owned and controlled by the Indigenous and Northern Affairs department of the Federal government, while Public Works and Government services is the current contracting authority.

Giant Mine: The Giant Mine was a gold mine located on the Ingraham Trail, 5 km north of Yellowknife, Northwest Territories.  Giant Mine is within the Kam Group, which is part of the Yellowknife greenstone belt.  Gold was discovered on the property and mineral claims staked in 1935 by Johnny Baker, but the true extent of the gold deposits were not known until 1944 when a massive gold-bearing shear zone was uncovered beneath the drift-filled Baker Creek Valley.

Ekati Diamond Mine: The Ekati Diamond Mine ("Ekati") is Canada's first surface and underground diamond mine.  It is located 310 km north-east of Yellowknife, Northwest Territories, and about 200 km south of the Arctic circle, near Lac de Gras.  Ekati is a joint venture between Dominion Diamond Corporation (80%), and the two geologists who discovered kimberlite pipes north of Lac de Gras, Chuck Fipke and Stewart Blusson each holding a 10% stake in the mine.

Question: What was a small gold mine 80 km north-east of Yellowknife, Northwest Territories, Canada at Gordon Lake, Camlaren Mine or Northland Pyrite Mine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mine_name": {
      "type": "string",
      "description": "The name of the mine identified."
    },
    "mine_type": {
      "type": "string",
      "description": "The primary type of mineral extracted from the mine."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "distance_from_yellowknife_km": {
          "type": "integer",
          "description": "The distance of the mine from Yellowknife in kilometers."
        },
        "direction_from_yellowknife": {
          "type": "string",
          "description": "The cardinal direction from Yellowknife."
        },
        "specific_lake_location": {
          "type": "string",
          "description": "The name of the lake where the mine is located."
        },
        "territory": {
          "type": "string",
          "description": "The territory or province where the mine is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the mine is located."
        }
      },
      "required": [
        "distance_from_yellowknife_km",
        "direction_from_yellowknife",
        "specific_lake_location",
        "territory",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mine_name",
    "mine_type",
    "location_details"
  ],
  "additionalProperties": false
}
