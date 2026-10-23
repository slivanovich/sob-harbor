{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEverest Public High School: Everest Public High School is a college preparatory, tuition-free, and public charter high school within the Sequoia Union High School District in Redwood City, California, United States.  The school, which was modeled after Summit Preparatory Charter High School in Redwood City, opened in August 2009 following State approval of the Everest charter.\n\nOakland Charter High School: Oakland Charter High School is a charter school in Oakland, California serving high school students.  It was established in 2007.  The school mascot is the matador.  It is part of the Amethod Public Schools system and the Oakland Unified School District.  In 2010–2011 the school had 121 students.  The school has since had, for the 2016–2017 school year, 445 students\n\nSacramento Charter High School: Sacramento Charter High School (\"Sac High\") is an independent public charter high school located in the Medical Center neighborhood, adjacent to the Alhambra Triangle and Oak Park neighborhoods in Sacramento, California.  Its charter was approved by the Sacramento City Unified School District's Board of Trustees on July 21, 2003.  The charter school occupies the school site formerly occupied by Sacramento High School, the second oldest high school west of the Mississippi.\n\nEvergreen Cemetery (Oakland, California): Evergreen Cemetery is a cemetery, crematorium and mausoleum located in Oakland, Alameda County, California, near the Eastmont Town Center and Mills College.  The cemetery is on a small hill, with a large combined mausoleum, crematorium and chapel at the top of the hill.  It is the second largest cemetery in Oakland, after the Mountain View Cemetery and Saint Mary Cemetery complex.  It is full, and closed to new interments, but still operates a crematorium.\n\nSummit Preparatory Charter High School: Summit Preparatory Charter High School (Summit Prep), part of the Sequoia Union High School District, is a college preparatory and charter high school that was founded in 2003.  Summit Prep is the first school founded by the charter management organization (CMO) Summit Public Schools, which has eight schools in the San Francisco Bay Area and three in Washington state.\n\nEastmont Town Center: Eastmont Town Center is a shopping mall and social services hub located on 33 acre bounded by Foothill Boulevard, Bancroft and 73rd Avenues, and Church Street, in the Eastmont neighborhood of East Oakland.  The mall opened in 1970 on the site of a 1920s-era Chevrolet automobile factory called Oakland Assembly.  Architect William Pereira designed the building.  It is physically almost next to, and by entry access a few blocks away from, the similarly sized Evergreen Cemetery.\n\nAmethod Public Schools: Amethod Public Schools (formerly Oakland Charter Academy Inc., doing business as Oakland Charter Academies) is a nonprofit charter school system with headquarters in Oakland, California.  The system operates Oakland Charter Academy (OCA) (Oakland's first charter school), Oakland Charter High School (OCHS), Downtown Charter Academy (DCA), Richmond Charter Academy (RCA) Benito Juarez Elementary School and John Henry High School, the latter three based in Richmond.  After a dramatic turnaround, Oakland Academy became the second public school in Oakland, California to win the National Blue Ribbon award.\n\nOakland Charter Academy: Oakland Charter Academy (OCA) originally Jingletown Charter School, is a charter school in Oakland, California serving middle school students.  Opened in 1994, it is the first and oldest charter school in Oakland and one of the first in California.  After a dramatic turnaround, it became the second public school in Oakland to win the National Blue Ribbon award.  The school was also designated the Hart Vision Charter School of the Year Award for 2009 by the California Charter Schools Association.  The Amethod Public Schools system grew out of Oakland Charter Academy, and now includes Oakland Charter High School and Downtown Charter Academy located in downtown Oakland.  The system also operates Benito Juarez Elementary School, Richmond Charter Academy and John Henry High School in Richmond.\n\nBay Area School of Enterprise: The Bay Area School of Enterprise, also known as BASE, is a charter high school founded in 2001 in Alameda, California.  It is the first youth-created charter high school in the United States.  It was created by 10 youth and 2 adults working in the afterschool program HOME Project to create a school for non traditional students.  BASE is a public charter school in the Alameda Unified School District.\n\nUniversity Preparatory Charter Academy: University Preparatory Charter Academy, also known as \"U-prep\" or \"UPREP\", was a charter high school in the Oakland Unified School District, California.  It was founded in 2001 by Isaac Haqq in the Eastmont Town Center.  The school doubled in size from some 130 to 260 students in 2004.  Haqq claimed \"We have made it cool to be smart at this school\".\n\nQuestion: University Preparatory Charter Academy, also known as \"U-prep\" or \"UPREP\", was a charter high school in the Oakland Unified School District, California, it was founded in 2001 by Isaac Haqq in the Eastmont Town Center, was founded in 2001 by Isaac Haqq in the Eastmont Town Center, was founded in what year, by Isaac Haqq in the Eastmont Town Center, a shopping mall and social services hub located on 33 acre bounded by Foothill Boulevard,?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the school.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the school was founded.\"\n    },\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who founded the school.\"\n    },\n    \"founding_location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the location where the school was founded.\"\n        },\n        \"location_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of establishment the founding location is (e.g., shopping mall, social services hub).\"\n        },\n        \"area_acres\": {\n          \"type\": \"integer\",\n          \"description\": \"The area of the founding location in acres.\"\n        },\n        \"boundaries\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of streets or features that bound the founding location.\"\n        }\n      },\n      \"required\": [\n        \"location_name\",\n        \"location_type\",\n        \"area_acres\",\n        \"boundaries\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"founding_year\",\n    \"founder_name\",\n    \"founding_location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The full name of the school."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the school was founded."
      },
      "founder_name": {
        "type": "string",
        "description": "The name of the person who founded the school."
      },
      "founding_location_details": {
        "type": "object",
        "properties": {
          "location_name": {
            "type": "string",
            "description": "The name of the location where the school was founded."
          },
          "location_type": {
            "type": "string",
            "description": "The type of establishment the founding location is (e.g., shopping mall, social services hub)."
          },
          "area_acres": {
            "type": "integer",
            "description": "The area of the founding location in acres."
          },
          "boundaries": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of streets or features that bound the founding location."
          }
        },
        "required": [
          "location_name",
          "location_type",
          "area_acres",
          "boundaries"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "school_name",
      "founding_year",
      "founder_name",
      "founding_location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
