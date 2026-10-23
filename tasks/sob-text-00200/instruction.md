{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDistant Cousins: Distant Cousins were an English band from Manchester.  Some journalists grouped them with the Madchester scene, though the music was a blend of soul and pop.  The group consisted of Doreen Edwards (vocals), Neil Fitzpatrick (ex-Smirks, guitar/sax), and \"Snuff\" (ex-Motivation, drums/percussion).  Edwards and Fitzpatrick wrote most of the band's songs.\n\nTrevor Johnson (footballer): Trevor Johnson (25 January 1935 – 10 November 2016) was an Australian rules football player in the Victorian Football League (VFL).\n\nDavid Isberg: David Isberg (born February 23, 1975) is a Swedish musician, most famous for having founded seminal Swedish progressive death metal band Opeth.  David Isberg is also known as DJ Dake, having a successful DJ career with independent and electronic music, often influenced by the Madchester scene.  He also DJs old school heavy, thrash, speed and death metal from the 1980s at Club Rocks in Stockholm on a monthly basis.\n\nCentral Station Design: Central Station Design is a Mancunian design company founded by Pat Carroll, Karen Jackson, and Matt Carroll.  It is usually associated with Factory Records and the Madchester scene of the early 1990s.  The company created album cover artwork and posters for Factory artists including The Happy Mondays, Black Grape, and James.  Their design for the Happy Mondays' \"Madchester Rave On E.P.\" in late 1989 became the iconic logo for the movement.  The Carrolls are cousins of Shaun and Paul Ryder of the Happy Mondays.\n\nThe Cygnet Ring: The Cygnet Ring were a band associated with the Madchester scene of 1989–1991 and best known for their song \"Love Crime\".  The band was founded by singer Rus Harrison who had previously been in a local indie band called Playing At Trains and had gained a cult following around the late 1980s.\n\nMadchester: Madchester is a music and cultural scene that developed in the Manchester area of the United Kingdom in the late 1980s, in which artists merged alternative rock with acid house culture and other sources, including psychedelia and 1960s pop.  The label was popularised by the British music press in the early 1990s, and included groups such as Happy Mondays, the Stone Roses, Inspiral Carpets, Northside, 808 State, James and The Charlatans, amongst others.\n\nParis Angels: Paris Angels were a seven piece band, hailing from Guide Bridge, Ashton-under-Lyne, Greater Manchester, associated with the Madchester scene of 1989 -1991.  Their music fused indie guitars with electronic dance music.  The band comprised Paul 'Wags' Wagstaff (later of Black Grape and the reformed Happy Mondays), Rikki Turner, Steven Taji, Scott Carey, Mark Adj, Jane Gill and Simon Worrall.\n\nMusic of the United Kingdom (1990s): Popular music of the United Kingdom in the 1990s continued to develop and diversify.  While the singles charts were dominated by boy bands and girl groups, British soul and Indian-based music also enjoyed their greatest level of mainstream success to date, and the rise of World music helped revitalise the popularity of folk music.  Electronic rock bands like The Prodigy and Chemical Brothers began to achieve a high profile.  Alternative rock reached the mainstream, emerging from the Madchester scene to produce dream pop, shoegazing, post rock and indie pop, which led to the commercial success of Britpop bands like Blur and Oasis; followed by a stream of post-Britpop bands like Travis and Feeder.\n\nTrevor Johnson (ice hockey): Trevor Johnson (born January 25, 1982 in Trail, British Columbia) is a Canadian-born italian professional ice hockey player who most recently played for Manchester Storm of the Elite Ice Hockey League.  He participated at the 2010 IIHF World Championship as a member of the Italian National men's ice hockey team.\n\nTrevor Johnson (designer): Trevor Johnson (born in Salford, Lancashire) is a Manchester-based graphic designer.  He started his career as a commercial illustrator and went on to become a freelance graphic designer, designing record sleeves and branding for Factory Records and Hacienda Nightclub Fac 51 which was instrumental in the creation of the Madchester music scene of the late 1980s and early 1990s.  His designs created as Trevor Johnson and with his partner business Johnson/Panas for factory records are documented in the Factory Records Catalogue of sleeves and merchandise and company promotional material.\n\nQuestion: Trevor Johnson was part of the Madchester scene, which were based out of where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person associated with the Madchester scene.\"\n    },\n    \"person_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person within the Madchester scene.\"\n    },\n    \"scene_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music and cultural scene.\"\n    },\n    \"scene_location\": {\n      \"type\": \"string\",\n      \"description\": \"The primary geographical area where the scene developed.\"\n    },\n    \"scene_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the scene developed.\"\n    },\n    \"scene_origin_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period when the scene developed.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_role\",\n    \"scene_name\",\n    \"scene_location\",\n    \"scene_country\",\n    \"scene_origin_period\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person associated with the Madchester scene."
      },
      "person_role": {
        "type": "string",
        "description": "The role of the person within the Madchester scene."
      },
      "scene_name": {
        "type": "string",
        "description": "The name of the music and cultural scene."
      },
      "scene_location": {
        "type": "string",
        "description": "The primary geographical area where the scene developed."
      },
      "scene_country": {
        "type": "string",
        "description": "The country where the scene developed."
      },
      "scene_origin_period": {
        "type": "string",
        "description": "The period when the scene developed."
      }
    },
    "required": [
      "person_name",
      "person_role",
      "scene_name",
      "scene_location",
      "scene_country",
      "scene_origin_period"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
