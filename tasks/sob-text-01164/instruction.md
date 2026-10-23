{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichelle Hoover: Michelle Hoover is an American writer and college instructor.  She is the author of \"The Quickening\" a 2010 novel.  She was born in Ames, Iowa, but currently lives in Boston, Massachusetts.  She was selected as the Philip Roth Writer-in-Residence at Bucknell University.  She was a MacDowell Fellow from the MacDowell Colony.  She has taught writing at Boston University and, since 2014, currently teaches at Brandeis University as the Fannie Hurst writer-in-residence.  She also teaches at GrubStreet, where she co-founded the Novel Incubator program.  She has an MFA from University of Massachusetts, Amherst.  In 2014 she was selected as the National Endowment of the Arts Individual Artist Fellowship.\n\nLisa Tessman: Lisa Tessman is a professor of Philosophy at Binghamton University.  She is also a faculty member in the Women, Gender, and Sexuality studies.  She currently teaches Graduate Programs in Social, Political, Ethical and Legal Philosophy or SPEL.  She also teaches undergraduate programs in Philosophy, and Philosophy, Politics and Law or PPL.\n\nStrabane: Strabane ( ; from Irish: \"An Srath Bán\" , meaning \"the white strath\" ), historically spelt Straban, is a town in West Tyrone, Northern Ireland.  It was the headquarters of the former Strabane District Council.\n\nSara Black: Sara Black (born 1978) is an American artist.  She currently teaches at Antioch College and previously taught at Northwestern University and the School of the Art Institute of Chicago.  Her \"performances, sculpture, installation, and collaborative works evolve around an interest in how materials move through the world and the shifting designation of values in American culture.\"  She holds a BFA in sculpture and installation from the University of Chicago, a Bachelor of Arts in environmental studies and art from The Evergreen State College, and a Bachelor of Fine Arts in sculpture and painting from the University of Wisconsin–Eau Claire.  She was a co-founder of the art collective \"Material Exchange\" which was active in Chicago until 2010 and currently works collaboratively with artists Jillian Soto, Charlie Vinz and others.  Her work has been widely exhibited in several galleries including the Smart Museum of Art, the \"Experimental Station\", the Museum of Contemporary Art, Chicago, the \"Betty Rymer Gallery\", Gallery 400, the Hyde Park Art Center, Portland State University, \"The Park Avenue Armory, New York\", \"The Museum of Contemporary Craft, Portland\", \"Eyebeam, New York\" and the \"DeVos Art Museum\".\n\nNotre Dame High School, Norwich: Notre Dame High School is a Roman Catholic secondary school and sixth form with academy status located in Norwich, England.  The current Headteacher is Mr Brian Conway.  The school was opened in 1864 and currently teaches around 1,400 pupils, 400 of whom are in the sixth form.  The Roman Catholic Diocese of East Anglia, Norfolk County Council, and the Department for Education all support Notre Dame High School.\n\nBrian Morton (American writer): Brian Morton (born 1955) is an American author, born in New York City.  He graduated from Sarah Lawrence College.  He has worked for \"Dissent\", where he became executive editor in 1995.  He currently teaches at Sarah Lawrence College, New York University and The Bennington Writing Seminars.  Morton grew up in Teaneck, New Jersey.\n\nApril Bernard: April Bernard (born 1956) is an American poet.  She was born and raised in New England, and graduated from Harvard University.  She has worked as a senior editor at \"Vanity Fair\", \"Premiere\", and \"Manhattan, inc\".  In the early 1990s, she taught at Amherst College.  In Fall 2003, she was Sidney Harman Writer-in-Residence at Baruch College.  She currently teaches at Skidmore College in Saratoga Springs, New York.  Her work has appeared in \"The New Yorker\", the \"Boston Review\", \"AGNI\", \"Ploughshares\", \"Parnassus\", and \"The New York Review of Books\".\n\nGeoffrey G. O'Brien: Geoffrey G. O'Brien (May 10, 1969) is an American poet.  Educated at Harvard University and the University of Iowa, O'Brien has taught at Brooklyn College, The University of Iowa Writers' Workshop and has been the Distinguished Poet in Residence at St. Mary's College of California and the Holloway Lecturer in the Practice of Poetry at the University of California, Berkeley, where he currently teaches.  He also teaches in the Prison University Project at San Quentin.\n\nBrian McGilloway: Brian McGilloway is an author hailing from Derry, Northern Ireland.  Born in 1974, he studied English at Queens University Belfast, where he was very active in student theatre, winning a national Irish Student Drama Association award for theatrical lighting design in 1996.  He is a former Head of English at St. Columb's College in Derry, but now teaches in Holy Cross College in Strabane.  McGilloway's debut novel was a crime thriller called \"Borderlands\".  \"Borderlands\" was shortlisted for a Crime Writers' Association Dagger award for a debut novel.\n\nPaul Spicer (musician): Paul Spicer (born 6 June 1952) is an English composer, conductor, and organist.  He taught choral conducting at the Royal College of Music and conducted the RCM Chamber Choir between 1995 and 2008.  He currently teaches conducting at the Birmingham Conservatoire and conducts their chamber choir which records for Somm Records.  He also teaches at Oxford and Durham universities.  Since 2004 he has been the conductor of the Petersfield Festival.  He was Senior Producer for BBC Radio 3 for the Midlands Region based in Birmingham between 1984 and 1990 after which he moved to be Artistic Director of the Lichfield Festival.  He also produced for various record companies over many years.  He founded the Finzi Singers in 1984 making many recordings for Chandos Records.  He conducts the Birmingham Bach Choir and the Whitehall Choir in London.  His compositions include two oratorios for Easter and for Advent with libretti by the Dr Tom Wright and a choral symphony 'Unfinished Remembering' (2014) to a libretto by Euan Tait commemorating the outbreak of World War 1.  He runs a series of choral courses under the banner of The English Choral Experience based mainly at Abbey Dore in Herefordshire.\n\nQuestion: Where is the college located that Brian McGilloway currently teaches at?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_of_interest\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"current_teaching_institution\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"location_details\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"town\": {\n              \"type\": \"string\"\n            },\n            \"region\": {\n              \"type\": \"string\"\n            },\n            \"country\": {\n              \"type\": \"string\"\n            }\n          },\n          \"required\": [\n            \"town\",\n            \"region\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location_details\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_location\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"person_of_interest\",\n    \"current_teaching_institution\",\n    \"final_answer_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_of_interest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "current_teaching_institution": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "location_details": {
            "type": "object",
            "properties": {
              "town": {
                "type": "string"
              },
              "region": {
                "type": "string"
              },
              "country": {
                "type": "string"
              }
            },
            "required": [
              "town",
              "region",
              "country"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "location_details"
        ],
        "additionalProperties": false
      },
      "final_answer_location": {
        "type": "string"
      }
    },
    "required": [
      "person_of_interest",
      "current_teaching_institution",
      "final_answer_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
