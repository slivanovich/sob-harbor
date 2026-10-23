{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCazadero Performing Arts Camp: Cazadero Performing Arts Camp (also known as Cazadero Music Camp, or Cazadero) is a performing arts camp located in the Sonoma redwoods in Northern California, United States.  Established in 1957 by then Berkeley High School band director Bob Lutt (who eventually was made executive director of the Berkeley Symphony), the first campers were a mixture of Berkeley High teens and members of the San Francisco Symphony.\n\nBlue Lake Fine Arts Camp: Blue Lake Fine Arts Camp is a Michigan nonprofit organization located in the Manistee National Forest that provides summer fine arts camp and international exchange programs in music, art, dance, and drama.\n\nList of South Fork Eel River crossings: The South Fork Eel River, a river in the northern part of the U.S. state of California, rises near Laytonville and flows about 105 mi in a northerly direction to its confluence with the Eel River near Weott.  Some major tributares of the mostly free-flowing river include Tenmile Creek, the East Branch South Fork Eel River near Benbow, and Hollow Tree Creek.  The river drains 689 mi2 and is said to be the primary river supporting coho salmon in the state.\n\nTonea Stewart: Stewart was born in Greenwood, Mississippi, the daughter of Hattie Juanita (Leonard) and Thomas Ezekiel Harris.  She has lived in Montgomery, Al since 1990.  She is a professional actress; play director, national museum exhibit director, tenured Professor and the Dean of the College of Visual & Performing Arts at Alabama State University.  As Dean of the College of Visual & Performing Arts, Tonea serves as administrator over the Department of Art, Music, and Theatre.  She also serves as professor, role model, motivator, and mentor to the students.  Since her arrival, the number of Theatre majors, minors, and the number of graduates from the Department of Theatre Arts have soared.  Recently the Department of Theatre Arts received the 2013 and 2014 Best Fine Arts Program Award from HBCU Digest.  Over seventy-five percent of the ASU theatre graduates have received full scholarships to major graduate universities such as Brown, Yale, University of California, Los Angeles, University of Louisville, to Washington State, New York University, and Louisiana State University to name a few.  Youth and adults from the Montgomery area and across the nation have been touched by her summer performance and enrichment camps: T.A.P.S.(Theatre Artists Performance School), Camp 3T (Teaching through Theatre), TTI(Technical Theatre Initiative), ARPAC (Adult Repertory Performing Arts Camp), and Camp Gifted for persons with disabilities.\n\nHog Farm: The Hog Farm is an organization considered to be America's longest running hippie commune.  With beginnings as a collective, first in North Hollywood, then, after moving, taking its name from its actual hog farm domicile in Tujunga, California.  The group, founded in the mid-1960s by peace activist and clown Wavy Gravy (formerly Hugh Romney) and his actress wife, Jahanara Romney (formerly Bonnie Jean Beecher), evolved into a \"mobile, hallucination-extended family\", active internationally in both music and politics.\n\nCamp Winnarainbow: Camp Winnarainbow is a circus and performing arts camp for all ages, founded and run by Wavy Gravy.  The camp adjoins the Hog Farm commune near Laytonville, California.\n\nStar Camp: Star Camp is a German performing arts camp that was created in 2009.  The camp kicked off in Büren, Nuremberg and Werbellinsee.  During the Easter holidays of 2010, Star Camp headed towards Helmarshausen in Bad Karlshafen, Hesse.  The Star Camp takes place every year.\n\nSongs of Hope Summer Camp: Songs of Hope is an international performing arts camp founded in 1990.  In a unique spin on traditional summer camp formats, its sponsoring organization, the Minnesota nonprofit organization, Sounds of Hope, Ltd., intentionally assembles international delegations of young people aged 10–13 from countries worldwide to create a global community within the camp.  Campers from the United States and countries worldwide join the country delegations and participate in a program of cultural sharing.  The country delegations are partly subsidized by corporate and foundation donors.  The project also emphasizes performance, with its campers presenting a three-week concert tour at the end of each summer’s six-week session, reaching audiences numbering in the thousands with performances celebrating world cultures and global unity.\n\nCelebrate Brooklyn!: Celebrate Brooklyn!  is one of New York City’s longest running, free, outdoor performing arts festivals. Launched in 1979 by the then Fund for the Borough of Brooklyn, as a catalyst for Brooklyn’s performing arts scene and to bring people back into Prospect Park after years of neglect, Celebrate Brooklyn was an anchor in the park’s revitalization and has become one of the city’s foremost summer cultural attractions.  Over the course of its history, the Festival has presented over 2,000 artists and ensembles reflective of the borough’s diversity, ranging from internationally acclaimed performers to emerging, cutting-edge artists.  The festival attracts upwards of 250,000 attendees from across New York City to the Prospect Park Bandshell each summer.  The festival is produced by BRIC, an organization that presents contemporary art, performing arts, and media programs throughout Brooklyn.\n\nInterlochen Center for the Arts: Interlochen Center for the Arts is a tax exempt, 501(c)(3) non-profit corporation, operating an arts education institution in northwest Michigan.  The center is situated on a 1,200 acre campus in Interlochen, Michigan, roughly 15 mi southwest of Traverse City.  Interlochen draws young people from around the world to study music, theater, dance, visual arts, creative writing, motion picture arts, and comparative arts.  Interlochen Center for the Arts is the umbrella organization for Interlochen Arts Camp (formerly the National Music Camp, founded 1928), Interlochen Arts Academy boarding high school (founded 1962), Interlochen Public Radio (founded 1963), Interlochen College of Creative Arts (founded 2004), and the \"Interlochen Presents\" performing arts series.\n\nQuestion: Camp Winnarainbow, is a circus and performing arts camp, it adjoins which organization, considered to be America's longest running hippie commune, near Laytonville, California?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"camp_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the performing arts camp.\"\n    },\n    \"adjoining_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization that the camp adjoins.\"\n    },\n    \"organization_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of organization.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A key characteristic or status of the organization.\"\n        },\n        \"location_context\": {\n          \"type\": \"string\",\n          \"description\": \"The geographical context of the organization's location relative to the camp.\"\n        },\n        \"founded_by\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Individuals credited with founding the organization.\"\n        },\n        \"founding_period\": {\n          \"type\": \"string\",\n          \"description\": \"The period when the organization was founded.\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"description\",\n        \"location_context\",\n        \"founded_by\",\n        \"founding_period\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"camp_name\",\n    \"adjoining_organization\",\n    \"organization_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "camp_name": {
        "type": "string",
        "description": "The name of the performing arts camp."
      },
      "adjoining_organization": {
        "type": "string",
        "description": "The name of the organization that the camp adjoins."
      },
      "organization_details": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of organization."
          },
          "description": {
            "type": "string",
            "description": "A key characteristic or status of the organization."
          },
          "location_context": {
            "type": "string",
            "description": "The geographical context of the organization's location relative to the camp."
          },
          "founded_by": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Individuals credited with founding the organization."
          },
          "founding_period": {
            "type": "string",
            "description": "The period when the organization was founded."
          }
        },
        "required": [
          "type",
          "description",
          "location_context",
          "founded_by",
          "founding_period"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "camp_name",
      "adjoining_organization",
      "organization_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
