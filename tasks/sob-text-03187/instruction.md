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
Finniss River: Finniss River is the name of two rivers in Australia, both named after colonial surveyor Boyle Travers Finniss.

Local government areas of the Northern Territory: The Northern Territory is a federal Australian territory in the central and central northern regions of Australia.  It is the third largest Australian federal division with an area of 1349129 km2 but the least populous with 211,945 inhabitants.  The Northern Territory is divided administratively into 17 Local government areas (LGAs) generally known as Councils who are responsible for providing local government services.

John Baker (Australian politician): John Baker (28 December 1813 – 19 May 1872) was an early South Australian pastoralist and politician.  He was the second Premier of South Australia, succeeding Boyle Travers Finniss; however, he only held office for 12 days from 21 August to 1 September 1857 before being succeeded by the third Premier of the colony, Robert Torrens.

William Scott-Elliot: William Scott-Elliot (sometimes incorrectly spelled Scott-Elliott) (1849-1919) was a theosophist who elaborated Helena Blavatsky's concept of root races in several publications, most notably "The Story of Atlantis" (1896) and "The Lost Lemuria" (1904), later combined in 1925 into a single volume called "The Story of Atlantis and the Lost Lemuria".  In 1893 he married Matilda (Maude) Louise Travers (1859-1929), daughter of Dr Robert Boyle Travers F.R.C.S., of Farsid Lodge, Rostellan, County Cork, Ireland.

Heard Island and McDonald Islands: The Territory of Heard Island and McDonald Islands (abbreviated as HIMI) is an Australian external territory comprising a volcanic group of barren Antarctic islands, about two-thirds of the way from Madagascar to Antarctica.  The group's overall size is 372 km2 in area and it has 101.9 km of coastline.  Discovered in the mid-19th century, the islands have been an Australian territory since 1947 and contain the country's only two active volcanoes.  The summit of one, Mawson Peak, is higher than any mountain on the Australian mainland.  The islands lie on the Kerguelen Plateau in the Indian Ocean.

Supreme Court of the Northern Territory: The Supreme Court of the Northern Territory is the superior court for the Australian Territory of the Northern Territory.  It has unlimited jurisdiction within the territory in civil matters, and hears the most serious criminal matters.  It is around the middle of the Australian court hierarchy.

B. T. Finniss: Boyle Travers Finniss (18 August 1807 – 24 December 1893) was the first Premier of South Australia, serving from 24 October 1856 to 20 August 1857.

Electoral district of Finniss: Finniss is an electoral district of the House of Assembly in the Australian state of South Australia.  It is named after B. T. Finniss, the first Premier of South Australia.  It covers a 5,875 km² regional area which includes Kangaroo Island, the Fleurieu Peninsula, and the towns of Kingscote, Middleton, Mount Compass, Penneshaw, Port Elliot, Sellicks Beach, Victor Harbor and Yankalilla.

Finniss Ministry: The Finniss Ministry was the 1st Ministry of the Government of South Australia, led by B. T. Finniss.  It commenced on 24 October 1856 with the introduction of responsible government in South Australia, and the nomination by Governor Richard Graves MacDonnell of Finniss, the appointed Chief Secretary, as the first Premier of South Australia.  The ministry operated for several months prior to the 1857 colonial election, which would elect the first House of Assembly.  The first House of Assembly was elected in March 1857 and met in April.  The Finniss Ministry was succeeded by the Baker Ministry on 21 August 1857, following their defeat on a confidence motion in the new House.

Northern Territory: The Northern Territory (abbreviated as NT) is a federal Australian territory in the central and central northern regions of Australia.  It shares borders with Western Australia to the west (129th meridian east), South Australia to the south (26th parallel south), and Queensland to the east (138th meridian east).  To the north, the territory is bordered by the Timor Sea, the Arafura Sea and the Gulf of Carpentaria.  Despite its large area—over 1349129 km2 , making it the third largest Australian federal division—it is sparsely populated.  The Northern Territory's population of 244,000 (2016) makes it the least populous of Australia's eight major states and territories, having fewer than half as many people as Tasmania.

Question: Boyle Travers Finniss was the very first Premier of which Australian territory?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "premier_full_name": {
      "type": "string",
      "description": "The full name of the premier."
    },
    "premiership_rank": {
      "type": "integer",
      "description": "The numerical rank of their premiership (e.g., 1 for first)."
    },
    "territory_or_state_name": {
      "type": "string",
      "description": "The name of the Australian territory or state where they served as premier."
    },
    "term_start_date": {
      "type": "string",
      "description": "The start date of their premiership term."
    },
    "term_end_date": {
      "type": "string",
      "description": "The end date of their premiership term."
    },
    "succeeded_by": {
      "type": "string",
      "description": "The name of the person who succeeded them as premier."
    }
  },
  "required": [
    "premier_full_name",
    "premiership_rank",
    "territory_or_state_name",
    "term_start_date",
    "term_end_date",
    "succeeded_by"
  ],
  "additionalProperties": false
}
