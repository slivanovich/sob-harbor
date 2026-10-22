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
Sakskøbing: Sakskøbing is a town with a population of 4,519 (1 January 2015) and a former municipality (Danish, "kommune") in Guldborgsund municipality in Region Sjælland on the northeast coast of the island of Lolland in south Denmark.  The former Sakskøbing municipality, including the small island of Vigsø, covered an area of 176 km², and had a total population of 9,299 (2005).  Its last mayor was Kaj Petersen a member of the Social Democrats ("Socialdemokraterne") political party.  The main town and the site of its municipal council is the town of Sakskøbing.  To the north is Tår's Cove ("Tårs Vig") and beyond that Rågø Strait ("Rågø Sund"), the waterway which separates Lolland from Zealand.  A finger of Rågø Strait cuts into the former municipality forming Sakskøbing Fjord and then Sakskøbing River ("Sakskøbing å"), which meanders through the former municipality, as well as through Nykøbing Falster and Nysted until it terminates near the town of Bregninge.

Aubonne: Aubonne is a municipality in the district of Morges in the canton of Vaud in Switzerland.

Ilanz: Ilanz (Romansh: Glion) is a former municipality in the district of Surselva in the Swiss canton of Graubünden.  The former municipality Ilanz was congruent with the town Ilanz, which is known now as Ilanz/Glion, as of 1 January 2014.  On 1 January 1978 the former municipality of Strada merged into the new municipality of Ilanz.  On 1 January 2014 the municipality of Ilanz and the surrounding municipalities Castrisch, Ladir, Luven, Pitasch, Riein, Ruschein, Schnaus, Sevgein, Duvin, Pigniu, Rueun and Siat merged into the new municipality of "Ilanz/Glion."

Beromünster: Beromünster is a municipality in the district of Sursee in the canton of Lucerne in Switzerland.  On 1 January 2004 the former municipality of Schwarzenbach merged into the municipality of Beromünster.  On 1 January 2009 the former municipality of Gunzwil merged into the municipality of Beromünster followed by Neudorf on 1 January 2013.

Davik: Davik is a former municipality in the traditional district of Nordfjord in Sogn og Fjordane county, Norway.  The former municipality existed from 1838 until 1964.  It encompassed all the lands surrounding the outer part of the large Nordfjorden on both sides of the fjord.  Davik was located in parts of the present-day municipalities of Vågsøy, Bremanger, and Eid.  The administrative center of the former municipality was the village of Davik which is located on the southern shore of the Nordfjorden, although some of the municipal services were based out of the village of Bryggja on the north side of the fjord, since that village was the largest village in Davik municipality.

Pizy: Pizy is a former municipality in the Swiss canton of Vaud.  It is located in the district of Morges.  On July 1, 2011 it was merged into Aubonne.

Røra: Røra is a village and former municipality in Nord-Trøndelag county, Norway.  It is located in the present-day municipality of Inderøy in the part of the municipality east of the Børgin fjord.  The former municipality existed from 1907 until 1962 and it bordered the municipality of Verdal to the south, Sparbu in Steinkjer municipality to the north, and Inderøy to the west.

Fana (municipality): Fana is a former municipality in Hordaland county, Norway.  The municipality was located in the central part of the Bergen Peninsula, south of the city of Bergen.  The administrative centre of the municipality was the village of Nesttun.  The roughly 200 km2 municipality existed from 1838 until 1972 when it had 44,402 residents, making it one of the most populous municipalities in the nation.  The area of the former municipality encompassed southern half of the present-day municipality of Bergen, it specifically included the present-day boroughs of Fyllingsdalen, Ytrebygda, and Fana, as well as the southern part of Årstad.

Vigra: Vigra is a former municipality in Møre og Romsdal county on the west coast of Norway.  It is located in the present-day Giske Municipality.  The former municipality was made up of the island of Vigra along with many smaller islets surrounding it.  The municipality existed from 1890 until 1964 when it was merged into Giske Municipality.  The administrative centre of the municipality was the village of Roald, and Vigra Church was the main church for the municipality.

Dirksland: Dirksland ( ) is a town and former municipality on Goeree-Overflakkee Island in the western Netherlands, in the province of South Holland.  The former municipality had a population of about 8,000 in 2007, and covered an area of about 74 km² of which about 19 km² was water.  The former municipality of Dirksland also included the communities of Herkingen, and Melissant.  On January 1, 2013, Dirksland merged with Goedereede, Middelharnis, and Oostflakkee into the new municipality of Goeree-Overflakkee.

Question: What municipality did former municipality Pizy merge with in Switzerland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "former_municipality": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the former municipality."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "merged_into_municipality": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the municipality it merged into."
        },
        "country": {
          "type": "string",
          "description": "The country where the municipality is located."
        },
        "location_details": {
          "type": "object",
          "properties": {
            "canton": {
              "type": "string",
              "description": "The canton of the municipality."
            },
            "district": {
              "type": "string",
              "description": "The district of the municipality."
            }
          },
          "required": [
            "canton",
            "district"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "country",
        "location_details"
      ],
      "additionalProperties": false
    },
    "merger_date": {
      "type": "string",
      "description": "The date when the merger occurred."
    }
  },
  "required": [
    "former_municipality",
    "merged_into_municipality",
    "merger_date"
  ],
  "additionalProperties": false
}
