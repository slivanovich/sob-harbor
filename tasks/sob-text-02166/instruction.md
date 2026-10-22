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
Garfield Street Historic District: The Garfield Street Historic District is a historic district on Garfield Street between Massachusetts Ave. and Oxford Street in Cambridge, Massachusetts.  The district encompasses a unified residential area developed between 1885 and 1891.  Garfield Street was laid out in 1883, and all but three of the houses built before 1891 still stand on the street.  The houses were built by different developers, and most were architect designed, and thus vary stylistically.  The streetview, however, is unified by uniform lot sizes, house heights, and setbacks.  Queen Anne styling predominates, with a variety of massing and roof lines; many houses have turrets and/or wraparound porches typical of that style.

Highclere Castle: Highclere Castle is a country house in the Jacobethan style by the architect Charles Barry, with a park designed by Capability Brown.  The 5000 acre estate is in Hampshire, England, about 5 mi south of Newbury, Berkshire.  It is the country seat of the Earl of Carnarvon, a branch of the Anglo-Welsh Herbert family.

City Architect of Birmingham: The City Architect of Birmingham was a high-ranking position within the Public Works department of Birmingham City Council and provided the holder with a lot of power in the planning decisions of Birmingham, especially in the post-war period in which Birmingham underwent enormous regeneration.  Combined with the City Engineer position, which was held by Sir Herbert Manzoni, the City Architect designed or had an important say in all city council building projects.

Nevil Story Maskelyne: Mervyn Herbert Nevil Story Maskelyne (3 September 1823 – 20 May 1911) was an English geologist and politician.

Hugh Hibbert: Hugh Washington Hibbert (4 October 1911 – 12 March 1985) was an English cricketer who played for Northamptonshire.  He was born in Kensington and died in Salisbury.  His dad, Mervyn Herbert played for Somerset amongst other teams.

Greater Second Street Historic District: The Greater Second Street Historic District is a nationally recognized historic district located in Ottumwa, Iowa, United States.  At the time of its nomination it contained 15 resources, which included 14 contributing buildings and one contributing site.  It is located on the northeast side of the central business district.  The commercial buildings located there are mostly architect designed, which gives each of them a unique appearance.  At the same time, it is a cohesive collection of buildings that exhibit early 20th century styles that are not found anywhere else in Ottumwa.  They were either built or they had a new facade added from 1903 to 1930.  Contributing buildings includes the Benson Block, the Benson Building, the J.W. Garner Building, and the headquarters building of the local newspaper, the "Ottumwa Courier".  The historic district was listed on the National Register of Historic Places in 2016.

Mervyn Herbert: The Honourable Mervyn Robert Howard Molyneux Herbert (27 December 1882 – 26 May 1929) was a career diplomat and a first-class cricket player.  He was born at Highclere Castle, Hampshire and he died at the British Embassy, Rome.

North Grand Avenue Residential Historic District: North Grand Avenue Residential Historic District is a nationally recognized historic district located in Spencer, Iowa, United States.  It was listed on the National Register of Historic Places in 2014.  At the time of its nomination the district consisted of 118 resources, including 96 contributing buildings, one contributing structure, 12 noncontributing buildings, and two noncontributing structures.  The district is an 11 block area north of the city's central business district.  North Grand is a tree-lined street divided by a landscaped boulevard, and features Art Deco light fixtures.  Its design was influenced by the City Beautiful movement.  The thoroughfare carries U.S. Route 71/18 traffic.  The contributing buildings are houses, garages, and four churches.  Architectural styles found here are Queen Anne, Victorian, Classical Revival, Colonial Revival, Greek Revival, American Four Square, Tudor Revival, Bungalow, and American Craftsman.  Many of the buildings are architect designed.  One of the houses in the district, the Adams-Higgins House (1884, 1912), was individually listed on the National Register in 1984.

Merv Thackeray: Mervyn Herbert (Merv) Thackeray (20 October 1925 – 7 June 2014) was an Australian politician.  He was an Australian Labor Party member of the Legislative Assembly of Queensland from 1957 until 1972, representing Keppel (1957–1960) and Rockhampton North (1960–1972).  He was disendorsed in January 1972 and ran unsuccessfully as an independent at the 1972 state election.

Cheongju National Museum: Cheongju National Museum is a national museum located in Sangdang-guCheongju, Chungcheongbuk-do, South Korea.  It opened on October 30, 1987.  Kim Swoo Geun, Korea’s most renowned architect designed the building.

Question: Which architect designed the building in which Mervyn Herbert was born ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_born_in_building": {
      "type": "string",
      "description": "The name of the person born in the specified building."
    },
    "building_name": {
      "type": "string",
      "description": "The name of the building where the person was born."
    },
    "architect_name": {
      "type": "string",
      "description": "The name of the architect who designed the building."
    },
    "architectural_style": {
      "type": "string",
      "description": "The architectural style of the building."
    }
  },
  "required": [
    "person_born_in_building",
    "building_name",
    "architect_name",
    "architectural_style"
  ],
  "additionalProperties": false
}
