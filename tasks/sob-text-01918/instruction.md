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
The Sands Family: The Sands Family is a Northern Irish musical family band originating from Mayobridge, County Down, Northern Ireland.  Their repertoire largely consists of their own compositions as well as traditional Irish songs.  The band is considered one of the most influential folk groups.  It showcases the famous Northern Irish folk singer-songwriter Tommy Sands as lead singer and songwriter and his brothers Ben Sands, Colum Sands and Eugene Sands and sister Anne Sands.  Eugene was killed in a car accident in 1975 and the formation became a 4-member band.  Tommy, Colum and Ben Sands have also successful solo careers as singers and musicians.

Dermot Seymour: Dermot Seymour (b. 1956, Belfast, Northern Ireland) is a Northern Irish artist.  He has been described as "a social realist, exploring the anxiety, bewilderment and absurdity of the situation in Northern Ireland and representing it with definite imagery but in an oblique and obscure way".  His social realist approach towards Northern Irish politics frequently involves a juxtaposition of images within the Irish landscape, particularly livestock, and religious and military symbols.  He lives in County Mayo and is a member of Aosdána.

Hugo Duncan: Hugo Duncan (Hugh Anthony Duncan) is a singer and BBC broadcaster born in Strabane, County Tyrone, Northern Ireland on 26 March 1950.  His nickname is "The wee man from Strabane" or "Uncle Hugo".

County Sligo: County Sligo ( , ) is an Irish county and part of the province of Connacht.  It is located in the Border Region.  Sligo is the administrative capital and largest town in the county.  Sligo County Council is the local authority for the county.  The population of the county is 65,393 according to the 2011 census making it the 3rd most populated county in the province.  It is noted for Benbulben Mountain, one of Ireland’s most distinctive natural landmarks.

M1 motorway (Republic of Ireland): The M1 motorway (Irish: "Mótarbhealach M1" ) is a motorway in Ireland.  It forms the large majority of the N1 national primary road connecting Dublin towards Belfast along the east of the island of Ireland.  The route heads north via Swords, Drogheda and Dundalk to the Northern Irish border just south of Newry in County Armagh, where it joins the A1 road and further on, the M1 motorway in Northern Ireland.  It also forms a significant part of the road connection between Dublin and the Northern Irish cities of Newry, and Lisburn.

Strabane: Strabane ( ; from Irish: "An Srath Bán" , meaning "the white strath" ), historically spelt Straban, is a town in West Tyrone, Northern Ireland.  It was the headquarters of the former Strabane District Council.

Country Afternoon with Hugo Duncan: Country Afternoon with Hugo Duncan is a country music radio programme, broadcast on BBC Radio Ulster Mondays to Fridays, 1.30pm-3pm.  The show features interviews with country singers and performers, and Hugo regularly takes the show on the road around Northern Ireland to meet the listeners.

Deputy Lieutenant: In the United Kingdom, a Deputy Lieutenant is a Crown appointment and one of several deputies to the Lord Lieutenant of a lieutenancy area: an English ceremonial county, Welsh preserved county, Scottish lieutenancy area, or Northern Irish county borough or county.

Sack of Cashel: The Sack of Cashel (also known as the Massacre of Cashel) was a notorious atrocity which occurred in the Irish County of Tipperary in the year 1647, during the Irish Confederate Wars, part of the Wars of the Three Kingdoms.  The town of Cashel was held by the Irish Catholic Confederate's Munster army and was besieged and taken by an English Protestant Parliamentarian army under Murrough O'Brien the Baron of Inchiquin.  The attack and subsequent sack of Cashel was one of the more brutal incidents of the wars of the 1640s in Ireland.

County Roscommon: County Roscommon (Irish: "Contae Ros Comáin" ) is a county in the western region of the Republic of Ireland.  It is also part of the province of Connacht.  It is the 11th largest Irish county by area and 27th most populous.  Its county town and largest town is Roscommon.  Roscommon County Council is the local authority for the county.  The population of the county is 64,436 according to the 2016 census.

Question: Hugo Duncan was born in a town in what Northern Irish county?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "birth_town": {
      "type": "string",
      "description": "The town where the person was born."
    },
    "birth_county": {
      "type": "string",
      "description": "The county where the person was born."
    },
    "country_region": {
      "type": "string",
      "description": "The country or region where the person was born."
    }
  },
  "required": [
    "person_name",
    "birth_town",
    "birth_county",
    "country_region"
  ],
  "additionalProperties": false
}
