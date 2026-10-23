{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMarlin Gray: Marlin A. Gray (September 29, 1967 – October 26, 2005) was convicted of aiding and abetting and executed by the U.S. state of Missouri by lethal injection.  His conviction was for being part of a group of four men who, on April 5, 1991, sexually assaulted and then murdered two sisters, and attempted to murder the sisters' cousin on the Chain of Rocks Bridge over the Mississippi River in St. Louis, Missouri.  Gray continued to protest his innocence saying that although he was at the bridge at the time, he was smoking cannabis in a nearby car.  On December 9, 1992, Gray was convicted of two counts of first-degree murder and was executed on October 26, 2005.  He maintained his innocence to the end.\n\nJens Söring: Jens Söring (born August 1, 1966 in Bangkok, Thailand) is a German citizen who in 1990 was convicted of two counts of first-degree murder in Virginia, United States.  Söring denies having committed the crime and has written a number of books about prison life and religion.\n\nMurder of Jim Pouillon: The murder of Jim Pouillon occurred on September 11, 2009.  Activist James Pouillon and businessman Michael Fuoss were each shot by the same killer, at separate locations.  Pouillon was killed while protesting abortion in front of Owosso High School in Owosso, Michigan, evidently the first time someone had been murdered while doing so.  Police arrested Harlan James Drake and charged him with both crimes.  Drake was later convicted of two counts of first-degree murder, and was subsequently sentenced to two life sentences.\n\nRichardson family murders: Three members of the Richardson family were murdered in Medicine Hat, Alberta, Canada in April 2006.  The murders were planned and committed by the family's 12-year-old daughter and her 23-year-old boyfriend Jeremy Steinke, now going by the name Jackson May.  The daughter and Steinke were each convicted on three counts of first-degree murder.  The daughter, who had turned 13 before being convicted, is thought to be the youngest person in Canada ever convicted of multiple first-degree murder counts.  Her 10-year sentence was completed on 6 May 2016.\n\nBarbecue murders: The barbecue murders, also known as the BBQ murders, refers to a 1975 double murder in Marin County, California.  Business consultant James \"Jim\" Olive and his wife Naomi were murdered in their home by their 16-year-old adopted daughter Marlene Olive and her 20-year-old boyfriend Charles \"Chuck\" Riley, who then attempted to dispose of the bodies by burning them in a barbecue pit at a nearby campground.  Riley was convicted of two counts of first-degree murder and received a sentence of death, which was later changed to life imprisonment with the possibility of parole.  Marlene Olive, tried as a juvenile, received a sentence of three to six years in a California Youth Authority juvenile facility, from which she was released at age 21 having served a little over four years.\n\n2014 Alaska state trooper killings: On May 1, 2014, two officers of the Alaska State Troopers were killed in Tanana after responding to a report of a resident brandishing a gun in an altercation over the private sale of a $150 couch.  The Fairbanks-based troopers, Sgt. Patrick Johnson and Trooper Gabriel Rich, had been featured in the National Geographic Channel program \"Alaska State Troopers\".  19-year-old Tanana resident Nathanial Lee Kangas was charged with two counts of first-degree murder and a single count of third-degree assault.\n\nWichita Massacre: The Wichita Massacre, also known as the Wichita Horror, was a spree of random robberies, assaults, rapes, and murders perpetrated from December 7 to 14, 2000 by brothers Reginald and Jonathan Carr against several people in the city of Wichita, Kansas.  In this period, the Carrs killed five people and a dog in the course of robberies and assaults, robbed another man, and severely wounded a woman.  The crimes shocked Wichitans, and incited a boom in sales of guns, locks, and home security systems.  The brothers were tried and convicted on multiple counts, including for kidnapping, robbery, rape, four counts of capital murder, and one count of first-degree murder.  They were both sentenced to death in October 2002.\n\nCharles Manson: Charles Milles Manson (born Charles Milles Maddox, November 12, 1934) is an American convicted mass murderer and former cult leader who led what became known as the Manson Family, a quasi-commune that arose in California in the late 1960s.  Manson's followers committed a series of nine murders at four locations in July and August 1969.  In 1971 he was found guilty of first-degree murder and conspiracy to commit murder for the deaths of seven people – most notably of the actress Sharon Tate – all of which were carried out by members of the group at his instruction.  Manson also received first-degree murder convictions for two other deaths.  Manson was originally sentenced to death, but his sentence was commuted to life imprisonment when California invalidated the state's death penalty statute in 1972.  He is currently serving multiple life sentences at California State Prison in Corcoran.\n\n2016 shootings of Des Moines police officers: In the early hours of November 2, 2016, two Iowa police officers, Justin Martin and Anthony Beminio, were killed in separate \"ambush-style\" shootings in and near Des Moines.  The perpetrator in both shootings, identified as 46-year-old Scott Michael Greene of Urbandale, Iowa, was apprehended by police hours later.  Greene pleaded guilty to two counts of first-degree murder and was sentenced to life without parole on May 20, 2017.\n\nThe Promise (2016 German film): The Promise (original title: \"Das Versprechen\") is a German documentary film directed by Marcus Vetter with Karin Steinberger.  The film tells the crime story of the double murder of Derek and Nancy Haysom on 30 March 1985 in Lynchburg, Virginia.  The film focuses on the two main protagonists Jens Söring, son of a German diplomat, and Elizabeth Haysom, the daughter of the murdered couple.  Both were sentenced to life in prison.  The film makes use of extensive original footage from press archives, as the two court cases were the first lawsuits to be broadcast nationwide on American television.  In the film, these recordings from 1985 to 1990 are combined with scenes shot during the making of the film, including interviews with Jens Söring, witnesses, the investigators involved in the case, lawyers, prosecutors and journalists.  In addition, extensive materials such as original crime scene photos and evidence, court transcripts, newspaper archives, love letters and diaries of the two main protagonists were evaluated in the film.\n\nQuestion: Which protagonist in the documentary film \"The Promise\" was convicted of two counts of first-degree murder?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the documentary film.\"\n    },\n    \"protagonist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the protagonist convicted.\"\n    },\n    \"conviction_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"crime_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of crime for which the protagonist was convicted.\"\n        },\n        \"count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of counts for the specified crime.\"\n        },\n        \"year_of_conviction\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the conviction occurred.\"\n        },\n        \"location_of_conviction\": {\n          \"type\": \"string\",\n          \"description\": \"The state or country where the conviction took place.\"\n        }\n      },\n      \"required\": [\n        \"crime_type\",\n        \"count\",\n        \"year_of_conviction\",\n        \"location_of_conviction\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"protagonist_name\",\n    \"conviction_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the documentary film."
      },
      "protagonist_name": {
        "type": "string",
        "description": "The name of the protagonist convicted."
      },
      "conviction_details": {
        "type": "object",
        "properties": {
          "crime_type": {
            "type": "string",
            "description": "The type of crime for which the protagonist was convicted."
          },
          "count": {
            "type": "integer",
            "description": "The number of counts for the specified crime."
          },
          "year_of_conviction": {
            "type": "integer",
            "description": "The year the conviction occurred."
          },
          "location_of_conviction": {
            "type": "string",
            "description": "The state or country where the conviction took place."
          }
        },
        "required": [
          "crime_type",
          "count",
          "year_of_conviction",
          "location_of_conviction"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "protagonist_name",
      "conviction_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
