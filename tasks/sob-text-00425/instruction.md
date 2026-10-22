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
Billy McEwan (footballer, born 1951): William Johnston McGowan McEwan (born 20 June 1951) is a Scottish former professional footballer and manager.  He had a 14-year playing career in the Scottish and English professional leagues, playing for seven different clubs.  McEwan then undertook a coaching career; he has managed six different English league clubs, plus one club on a caretaker basis twice.  McEwan was most recently the manager of Antigua Barracuda but left the post in 2011.

Craig McEwan (boxer): Craig McEwan (born 13 April 1982) is a Scottish boxer raised in Wester Hailes, Edinburgh, Scotland.  He began attending boxing classes at Clovenstone Amateur Boxing Club, aged seven, coached by his father Rab.  McEwan turned professional in 2006 and is currently fighting at middleweight.  He holds a career record of 21 wins, with 10 by way of knockout and four losses.

McEwan Hall: The McEwan Hall is the graduation hall of the University of Edinburgh, in Edinburgh, the capital of Scotland.  It was presented to the University in 1897 by William McEwan, brewer and politician, at a cost of £115,000.  Sir Robert Rowand Anderson was the architect.  The McEwan Hall is a Grade A listed building.

William McEwan Younger: Sir William McEwan Younger, 1st Baronet (6 September 1905 – 15 April 1992) was a Scottish brewer and political activist.

McEwan Fraser Legal: McEwan Fraser Legal is a Scottish solicitors and estate agency, which sells both residential properties and commercial properties throughout Scotland.  It is headquartered in Edinburgh, and has a staff of around 160.  It was founded as McEwan Fraser Legal Services LLP in 2009 by Ken McEwan and former footballer Scott Fraser.

Drybrough &amp; Co: Drybrough & Co was a brewery in Edinburgh, Scotland, from 1895 to 1987.  Members of the Drybrough family had been brewing beer in Edinburgh since before 1750.  In 1892 they moved to a new factory at a greenfield site in Craigmillar, designed by Robert Hamilton-Paterson.  It was the second brewery established in Craigmillar.  The new company was established in 1895 and sold beer in south and west Scotland.  They also supplied a brewery in Northumberland and one in Dundee.  In 1965 they were taken over by Watney Mann, and in 1987 the company was bought by Allied Lyons, who closed the brewery.  Production ended on 23 January 1987.

Craig McEwan (footballer): Craig George McEwan (born 3 October 1977 in Glasgow) is a Scottish footballer who is currently player-manager of Glenafton Athletic in the Scottish Junior Football Association, West Region.  A right full-back, McEwan has played in the Scottish Football League First Division for Raith Rovers and Ayr United and is a former Scotland under-21 international.

Willie McEwan (golfer): William McEwan (1872 – 2 May 1931) was a Scottish professional golfer.  McEwan placed ninth in the 1890 Open Championship which was held 11 September at Prestwick Golf Club in Prestwick, South Ayrshire, Scotland.  His share of the purse was £1.

McEwan's: McEwan's is a brand of beer that originated in Edinburgh, Scotland and is owned by the English brewer Wells & Youngs.

William McEwan: William McEwan ( ) (16 July 1827 – 12 May 1913) was a Scottish politician and brewer.  He founded the Fountain Brewery in 1856, served as a member of parliament (MP) from 1886 to 1900, and funded the construction of the McEwan Hall at the University of Edinburgh.

Question: William McEwan, was a Scottish politician and brewer, he founded the Fountain Brewery in which year, which distributes McEwan's is a brand of beer that originated in Edinburgh, Scotland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of occupations held by the person."
        }
      },
      "required": [
        "name",
        "occupations"
      ],
      "additionalProperties": false
    },
    "founded_entity": {
      "type": "object",
      "properties": {
        "entity_type": {
          "type": "string",
          "description": "The type of entity founded (e.g., brewery, company)."
        },
        "entity_name": {
          "type": "string",
          "description": "The name of the entity founded."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the entity was founded."
        }
      },
      "required": [
        "entity_type",
        "entity_name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "related_brand_info": {
      "type": "object",
      "properties": {
        "brand_name": {
          "type": "string",
          "description": "The name of the related beer brand."
        },
        "brand_origin_city": {
          "type": "string",
          "description": "The city where the brand originated."
        },
        "brand_origin_country": {
          "type": "string",
          "description": "The country where the brand originated."
        },
        "current_owner": {
          "type": "string",
          "description": "The current owner of the brand."
        }
      },
      "required": [
        "brand_name",
        "brand_origin_city",
        "brand_origin_country",
        "current_owner"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_details",
    "founded_entity",
    "related_brand_info"
  ],
  "additionalProperties": false
}
