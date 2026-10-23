{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nParkside, Barrow-in-Furness: Parkside is an area and electoral ward of Barrow-in-Furness, Cumbria, England.  It is bordered by Hindpool, Ormsgill, Hawcoat, Newbarns and Risedale and had a population of 5,742 in 2001, reducing to 5,584 at the 2011 Census.  It is one of the town's most centralised wards and contains Barrow's main park (hence the ward's name), as well as the newly established Furness Academy.  Abbey Road - Barrow's principal road runs down the entire western side of Parkside.  The majority of housing to the west of Abbey Road is terraced and semi-detached, whilst the eastern side of Parkside is predominantly parkland and fields with the exception of some semi and detached housing.  There are a number of place of worship in Parkside including Abbey Road Baptist Church, Spring Mount Christian Fellowship and Trinity Church Centre.  Barrow's first synagogue was founded in 1902 on Abbey Road although it closed less than twenty years later.\n\nJohn Whinnerah Institute: The John Whinnerah Institute is a Grade II listed Art Deco building and former educational establishment located on Abbey Road in Barrow-in-Furness, England.  Having been constructed between 1937 and 1938 on the site of the demolished Jute Works it is the newest listed structure in the town, despite this it was drastically altered in 2004 when the entire interior was demolished to accommodate new retail units leaving only the Abbey Road and Hindpool Road facades.\n\nHouldsworth Working Men's Club: Houldsworth Working Men's Club is a club in Stockport, Greater Manchester, England (grid reference [ SJ895935] ).  Designed by the famed Alfred Waterhouse and completed in the late 19th century, it is still used as a working men's club today.  An important local structure, it is now a Grade II* listed building.\n\nTommy Sale (rugby league): Tommy Sale {'1': \", '2': \", '3': \", '4': \"} (21 July 1918 – 3 January 2016) was an English rugby league player who played for Leigh (twice), Warrington (Heritage № 468), Wigan Road Working Men's Club ARLFC, and Widnes (Captain).\n\nBarrow-in-Furness: Barrow-in-Furness ( ; commonly known as Barrow) is a town and borough in Cumbria, England.  Historically part of Lancashire, it was incorporated as a municipal borough in 1867 and merged with adjacent districts in 1974 to form the Borough of Barrow-in-Furness.  At the tip of the Furness peninsula, close to the Lake District, it is bordered by Morecambe Bay, the Duddon Estuary and the Irish Sea.  In 2011, Barrow's population was 57,000, the second largest urban area in Cumbria after Carlisle.  Natives of Barrow, as well as the local dialect, are known as Barrovian.\n\nVictoria Working Men's Club: The Victoria Working Men's Club was a working men's club at 275 Sandycombe Road in Kew, Richmond, London which operated from 1892 until 2015, when the building it occupied was sold to a property developer.  In February 2017 Richmond upon Thames Council approved a planning application to demolish the building, and erect a new community building and six flats.\n\nWoolston W.M.C.: Woolston W.M.C. (Woolston Working Men's Club) was an association football club based in Woolston, Christchurch, New Zealand.  It was formed in 1951 as Waterside, before the name was changed to Woolston Working Men's Club in 1969.  The team played in the New Zealand National Soccer League in 1978 and 1981, being relegated back into the regional leagues at the end of both seasons.\n\nAbbey Road Working Men's Club: Abbey Road Working Men's Club (also known as Lord's Tavern and the House of Lords) is a Grade II listed building located at Abbey Road close to Ramsden Square in Barrow-in-Furness, Cumbria, England.  Design by architect HA Darbishire it was completed in 1871 and extended in the early 20th century, notable features included an ornate hipped roof with multiple oval dormers and an engraving of the Borough Coat of Arms.  During the building's lifetime it functioned as a social club and later public house.\n\nWorking Men's Club and Institute Union: The Working Men's Club and Institute Union (CIU or C&IU) is a voluntary association of private members' clubs in Great Britain & Northern Ireland, with about 1,800 associate clubs.  One club in the Republic of Ireland, the City of Dublin Working Men's Club is also affiliated.  Most social clubs are affiliated to the CIU.\n\nLangham Working Men's Club: The Langham Working Men’s Club is a traditional working men's club in the north London neighbourhood of Harringay\n\nQuestion: In 2011 what was the population of the town in which Abbey Road Working Men's Club is located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town where the club is located.\"\n    },\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the working men's club.\"\n    },\n    \"population_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year for which the population is reported.\"\n    },\n    \"population_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The population count of the town in the specified year.\"\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"club_name\",\n    \"population_year\",\n    \"population_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the town where the club is located."
      },
      "club_name": {
        "type": "string",
        "description": "The name of the working men's club."
      },
      "population_year": {
        "type": "integer",
        "description": "The year for which the population is reported."
      },
      "population_count": {
        "type": "integer",
        "description": "The population count of the town in the specified year."
      }
    },
    "required": [
      "town_name",
      "club_name",
      "population_year",
      "population_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
