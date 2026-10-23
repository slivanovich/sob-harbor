{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLa Sombra: La Sombra de Chicago or La Sombra de Tony Guerrero or even the Windy City Boys is a Tejano band founded by Tony Guerrero.  Originally from the Chicago suburb of Aurora, Illinois, the group gained national acclaim and success after moving to Corpus Christi, Texas, the headquarters of their label, Freddie Records.\n\nSteve Grand: Steve Grand (born February 28, 1990) is an American singer, songwriter and model from Lemont, Illinois, a Chicago suburb.  He became an overnight internet celebrity and the music video of his first hit \"All-American Boy\" went viral on YouTube in less than a week in July 2013.  This attention landed Grand on \"Good Morning America\", CNN and other national media.  On \"Good Morning America\" Steve shared how difficult it was for him to come out to his parents as a high school student—saying with obvious emotion \"I felt like I was a shame to my parents and that there was no way I could ever make them proud.\" .  Buzzfeed ranked the video on its list of the \"24 Most Brilliant Music Videos from 2013\", and \"Out\" magazine named Grand to its annual \"Out100\" list of the year's most compelling LGBT people.  In addition to being a musician, Grand has become an active figure in the LGBT equality movement.  He released his debut album titled \"All American Boy\" financed by a successful \"Kickstarter\" public funding campaign.\n\nScreeching Weasel: Screeching Weasel is an American punk rock band originally from the Chicago suburb of Prospect Heights, Illinois.  The band was formed in 1986 by Ben Weasel and John Jughead.\n\nChevelle (band): Chevelle is an American alternative metal band that formed in 1995 in the Chicago suburb of Wildwood, Illinois.  The band was originally composed of brothers: Pete Loeffler (lead vocals and guitar), Sam Loeffler (drums and percussion) and Joe Loeffler (bass and backing vocals).  When Joe left the band in 2005, Geno Lenardo subbed-in as the bassist until he was replaced by Pete and Sam's brother-in-law, Dean Bernardini.\n\nThe Discovery (album): The Discovery is the second studio album by the Chicago-based American band Born of Osiris.  It was released through Sumerian Records on March 22, 2011.  It is also the first album by the band to use seven string guitars, and was produced solely by members of the band.  The demo was produced by Periphery's Misha \"Bulb\" Mansoor.  This is the only album to feature guitarist Jason Richardson.\n\nBorn of Osiris: Born of Osiris is an American deathcore band, formed in 2003 in Palatine, a suburb of Chicago.  The group underwent several name changes, including Diminished (2003–2004), Your Heart Engraved (2004–2006), and Rosecrance (2006–2007), before finally settling on Born of Osiris in 2007, basing the name on the Egyptian deity Osiris, and the tale of his son Horus.\n\nPezband: Pezband was an American power pop band formed in 1971 in the Chicago suburb of Oak Park, Illinois.\n\nThe Printhouse: The Printhouse is an American company headquartered in the Chicago suburb of Palatine, Illinois.  The Printhouse was formed when a company, Qualay International changed names in 1995 to The Printhouse.  They are a provider of commercial printing and paperboard packaging.  The Printhouse has designed a unique, fully online proofing system.  This proofing method includes QR codes.\n\nFall Out Boy: Fall Out Boy is an American rock band formed in Wilmette, Illinois, a suburb of Chicago, in 2001.  The band consists of lead vocalist and rhythm guitarist Patrick Stump, bassist Pete Wentz, lead guitarist Joe Trohman, and drummer Andy Hurley.  The band originated from Chicago's hardcore punk scene, with which all members were involved at one point.  The group was formed by Wentz and Trohman as a pop punk side project of the members' respective hardcore bands, and Stump joined shortly thereafter.  The group went through a succession of drummers before landing Hurley and recording the group's debut album, \"Take This to Your Grave\" (2003).  The album became an underground success and helped the band gain a dedicated fanbase through heavy touring, as well as some moderate commercial success.  \"Take This to Your Grave\" has commonly been cited as an influential blueprint for pop punk music in the 2000s.\n\nChicago (band): Chicago is an American rock band formed in 1967 in Chicago, Illinois.  The self-described \"rock and roll band with horns\" began as a politically charged, sometimes experimental, rock band and later moved to a predominantly softer sound, generating several hit ballads.  The group had a steady stream of hits throughout the 1970s and 1980s.  Since at least 2008, \"Billboard\" has shown Chicago to be the \"greatest of all time\" American band in singles chart success, and since 2015, the \"greatest of all time\" American band in album chart success as well.  Chicago is one of the longest-running and most successful rock groups, and one of the world's best-selling groups of all time, having sold more than 100 million records.\n\nQuestion: The Discovery is an album by the band formed in what Chicago suburb?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that released the album.\"\n    },\n    \"formation_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city or suburb where the band was formed.\"\n        },\n        \"is_chicago_suburb\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the formation location is a Chicago suburb.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"is_chicago_suburb\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_name\",\n    \"band_name\",\n    \"formation_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that released the album."
      },
      "formation_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city or suburb where the band was formed."
          },
          "is_chicago_suburb": {
            "type": "boolean",
            "description": "Indicates if the formation location is a Chicago suburb."
          }
        },
        "required": [
          "city",
          "is_chicago_suburb"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_name",
      "band_name",
      "formation_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
