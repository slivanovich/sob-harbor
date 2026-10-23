{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHatfield War Memorial: The Hatfield War Memorial is a war memorial beside the Great North Road in Hatfield, Hertfordshire.  It was one of 24 war memorials in England designed by Sir Herbert Baker, that were designated as a national collection by Historic England in 2017.  The memorial is located near the gates of Hatfield House, and close to Hatfield railway station.  It was unveiled in 1921, to commemorate 139 men from Hatfield killed on service during the First World War.  A brick pavilion records the names of the dead, with further names added after the Second World War.\n\nYork City War Memorial: The York City War Memorial is a First World War memorial designed by Sir Edwin Lutyens and located in York in the north of England.  Proposals for commemorating York's war dead originated in 1919 but proved controversial.  Initial discussions focused on whether a memorial should be a monument or should take on some utilitarian purpose.  Several functional proposals were examined until a public meeting in January 1920 opted for a monument.  The city engineer produced a cost estimate and the war memorial committee engaged Lutyens, who had recently been commissioned by the North Eastern Railway (NER) to design their own war memorial, also to be sited in York.  Lutyens' first design was approved, but controversy enveloped proposals for both the city's and the NER's memorials.  Members of the local community became concerned that the memorials as planned were not in keeping with York's existing architecture, especially as both were in close proximity to the ancient city walls, and that the NER's memorial would overshadow the city's.  Continued public opposition forced the committee to abandon the proposed site in favour of one on Leeman Road, just outside the walls, and Lutyens submitted a new design of a War Cross and Stone of Remembrance to fit the location.  This was scaled back to the cross alone due to lack of funds.\n\nWelham Green: Welham Green is a village in the parish of North Mymms, Hertfordshire, England.  It is situated a mile to the west of the Great North Road coaching route that used to run through the neighbouring hamlet of Bell Bar from London to York and the north.  The Great North Road is now by-passed by the A1(M).  Even so, Welham Green has developed into a large village over the last 20 years, helped by the 1986 opening of its own railway station between Brookmans Park and Hatfield on the East Coast Main Line.  Recent housing development has portended the joining of the village with the neighbouring town of Hatfield.  Some residents, including the North Mymms Green Belt Society, wishing to maintain Welham Green's character, have resisted such development.\n\nBrocket Hall: Brocket Hall is a Grade I-listed classical country house set in a large park at the northern end of the urban area of Hatfield in Hertfordshire, England.  The estate is equipped with two golf courses and seven smaller listed buildings, apart from the main house.\n\nThe Wrestlers, Hatfield: The Wrestlers is a grade II listed public house on the Great North Road, Hatfield, in Hertfordshire.  The building has an eighteenth-century chequered red brick front based on a sixteenth-century core.\n\nStanage Park: Stanage Park is a Grade II*-listed English country house set in a large park located some 3 mi east of Knighton, Powys near the settlement of Heartsease.  The extensive parkland and the house were laid out by Humphry Repton and his son, John Adey Repton, in the early nineteenth century.  Repton's picturesque parkland improvements, castellated house and enclosed garden survive almost intact.  The estate is the last and most complete of his three recognized Welsh landscape commissions.\n\nCivilian War Memorial: The Memorial to the Civilian Victims of the Japanese Occupation, usually called the Civilian War Memorial (Chinese: 日本占领时期死难人民纪念碑 ; Malay: \"Tugu Peringatan Bagi Mangsa Awam Pemerintahan Jepun\" ) is a war memorial and heritage landmark in Singapore.  It was built in memory of the civilians killed during the Japanese occupation of Singapore during World War II.  The Civilian War Memorial sits on serene parkland in the midst of busy city traffic near Singapore's Padang and City Hall.  Located within the War Memorial Park at Beach Road within the Central Area, Singapore's central business district, it is usually easy to spot in most backdrops encompassing the CBD landscape.\n\nHatfield House: Hatfield House is a country house set in a large park, the Great Park, on the eastern side of the town of Hatfield, Hertfordshire, England.  The present Jacobean house, a leading example of the prodigy house, was built in 1611 by Robert Cecil, First Earl of Salisbury and Chief Minister to King James I and has been the home of the Cecil family ever since.  It is a prime example of Jacobean architecture.  The estate includes extensive grounds and surviving parts of an earlier palace.  The house, currently the home of Robert Gascoyne-Cecil, 7th Marquess of Salisbury, is open to the public.\n\nMachine Gun Corps Memorial: The Machine Gun Corps Memorial, also known as The Boy David, is a memorial to the casualties of the Machine Gun Corps in the First World War.  It is located on the north side of the traffic island at Hyde Park Corner in London, near the Wellington Arch, an Equestrian statue of the Duke of Wellington, the Royal Artillery Memorial, the New Zealand War Memorial, and the Australian War Memorial.\n\nThe Red Lion, Hatfield: The Red Lion is a grade II listed public house and former hotel on the Great North Road, Hatfield, in Hertfordshire.  The building dates from the late eighteenth century with nineteenth century additions and a large 1950s rear extension.\n\nQuestion: The Hatfield War Memorial is a war memorial beside the Great North Road in Hatfield, Hertfordshire, the memorial is located near the gates of which country house set in a large park, the Great Park, on the eastern side of the town of Hatfield, Hertfordshire, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"memorial_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the war memorial.\"\n    },\n    \"nearby_landmark\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the nearby landmark.\"\n        },\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the nearby landmark.\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the memorial is located.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the memorial is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the memorial is located.\"\n        }\n      },\n      \"required\": [\n        \"town\",\n        \"county\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"memorial_name\",\n    \"nearby_landmark\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "memorial_name": {
        "type": "string",
        "description": "The name of the war memorial."
      },
      "nearby_landmark": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of the nearby landmark."
          },
          "name": {
            "type": "string",
            "description": "The name of the nearby landmark."
          }
        },
        "required": [
          "type",
          "name"
        ],
        "additionalProperties": false
      },
      "location": {
        "type": "object",
        "properties": {
          "town": {
            "type": "string",
            "description": "The town where the memorial is located."
          },
          "county": {
            "type": "string",
            "description": "The county where the memorial is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the memorial is located."
          }
        },
        "required": [
          "town",
          "county",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "memorial_name",
      "nearby_landmark",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
