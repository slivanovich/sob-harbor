{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSeventh Avenue (IND Queens Boulevard Line): Seventh Avenue is a station on the IND Sixth Avenue Line and the IND Queens Boulevard Line of the New York City Subway.  Located at the intersection of Seventh Avenue and 53rd Street in Manhattan, it is served by the D and E trains at all times, and the B train weekdays.  The station is announced as Seventh Avenue–53rd Street, in the style of other stations that orient east-west along 53rd Street (such as Fifth Avenue/53rd Street and Lexington Avenue–53rd Street), as well as to prevent confusion with Seventh Avenue along Flatbush Avenue in Brooklyn, which is also served by the B.\n\nCarnegie Hall: Carnegie Hall ( , also frequently or ) is a concert venue in Midtown Manhattan in New York City, United States, located at 881 Seventh Avenue, occupying the east side of Seventh Avenue between West 56th Street and West 57th Street, two blocks south of Central Park.\n\nSeventh Avenue (BMT Brighton Line): Seventh Avenue is a station on the BMT Brighton Line of the New York City Subway, located at the intersection of Seventh Avenue, Park Place and Flatbush Avenue in Park Slope and Prospect Heights, Brooklyn.  It is served by the Q train at all times and the B train on weekdays.  This is one of two stations on the B train named \"Seventh Avenue\"; the other is Seventh Avenue–53rd Street on the IND Sixth Avenue Line in Manhattan.\n\n28th Street (IRT Broadway–Seventh Avenue Line): 28th Street is a local station on the IRT Broadway–Seventh Avenue Line of the New York City Subway.  Located at the intersection of 28th Street and Seventh Avenue in Manhattan, it is served by the 1 train at all times, and by the 2 train during late nights and weekends.\n\nSeventh Avenue Line (Manhattan surface): The Seventh Avenue Line is a surface public transit line in Manhattan, New York City, United States, connecting Lower Manhattan with Central Park along Seventh Avenue.  Once a streetcar line, it is now part of the southbound direction of the M10 and M20 bus routes.\n\nGeeta Novotny: Geeta Novotny (born Geeta Bhatnagar) is an American mezzo-soprano, actor, published writer and columnist.  As a classical singer, Novotny has performed principal roles nationally with opera companies and symphony orchestras from the stages of New York City's Carnegie Hall and the American Ballet Theatre at the Metropolitan Opera to the stages of the Los Angeles Opera and the Aspen Music Festival.  Novotny has sung lead vocals on film soundtracks and has a career as a principal stage and film actor.  She is also a project leader and roster artist for the charitable organization Sing For Hope.  Novotny is an artist on the David Lynch Foundation Music Online Record Label which released an exclusive audio and video track of Novotny performing the beautiful classic song, the Gounod/Bach \"Ave Maria\" - with Andy Summers, the guitarist of the band The Police on electric guitar.\n\n810 Seventh Avenue: 810 Seventh Avenue is a Class-A office skyscraper located a few blocks north of Times Square on Seventh Avenue between 52nd and 53rd streets within Midtown Manhattan in New York City, United States.  It is owned by SL Green Realty Corp. after its acquisition of Reckson Associates Realty Corp., completed in January 2007.  The back of the building is situated on Broadway, diagonally across Broadway and 53rd from CBS's Ed Sullivan Theater, home of \"The Late Show with Stephen Colbert\".\n\nIRT Broadway–Seventh Avenue Line: The IRT Broadway–Seventh Avenue Line (also known as the Seventh Avenue Line or the West Side Line) is a New York City Subway line.  It is one of several lines that serves the A Division (IRT), stretching from South Ferry in Lower Manhattan north to Van Cortlandt Park–242nd Street in Riverdale, Bronx.  The Brooklyn Branch, known as the Wall and William Streets Branch during construction, from the main line at Chambers Street southeast through the Clark Street Tunnel to Borough Hall in Downtown Brooklyn, is also part of the Broadway–Seventh Avenue Line.\n\nSeventh Avenue (IND Culver Line): Seventh Avenue, occasionally referred to as Seventh Avenue–Park Slope, is an express station on the IND Culver Line of the New York City Subway, located at Seventh Avenue and Ninth Street in the Park Slope neighborhood of Brooklyn.  It is served by the F and G trains at all times.\n\n133rd Street (Manhattan): 133rd Street is a street in Manhattan and the Bronx, New York City.  In Harlem, Manhattan, it begins at Riverside Drive on its western side and crosses Broadway, Amsterdam Avenue, and ends at Convent Avenue, before resuming on the eastern side, crossing Seventh Avenue, and ending at Lenox Avenue.  In Port Morris in the Bronx, it runs from Bruckner Boulevard/St. Ann's Place to Locust Avenue.  The block between Seventh Avenue and Lenox Avenues was once a thriving night spot, known as \"Swing Street\", with numerous cabarets, jazz clubs, and speakeasies.  The street is described in modern times as \"a quiet stretch of brownstones and tenement-style apartment houses, the kind of block that typifies this section of central Harlem\".\n\nQuestion: Geeta Novotny performed on what stage located at 881 Seventh Avenue in New York City, United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"performer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the performer.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"venue\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the venue where the performance took place.\"\n        },\n        \"address\": {\n          \"type\": \"string\",\n          \"description\": \"The street address of the venue.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the venue is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the venue is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"address\",\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"performance_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"role_or_type\": {\n          \"type\": \"string\",\n          \"description\": \"The role or type of performance given by the artist at the venue.\"\n        }\n      },\n      \"required\": [\n        \"role_or_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"performer\",\n    \"venue\",\n    \"performance_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "performer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the performer."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "venue": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the venue where the performance took place."
          },
          "address": {
            "type": "string",
            "description": "The street address of the venue."
          },
          "city": {
            "type": "string",
            "description": "The city where the venue is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the venue is located."
          }
        },
        "required": [
          "name",
          "address",
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "performance_details": {
        "type": "object",
        "properties": {
          "role_or_type": {
            "type": "string",
            "description": "The role or type of performance given by the artist at the venue."
          }
        },
        "required": [
          "role_or_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "performer",
      "venue",
      "performance_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
