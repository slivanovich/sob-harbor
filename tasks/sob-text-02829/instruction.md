{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGary James: Gary Harry James, popularly known as 'Harry' James (born 14 December 1960 in England) is a British drummer best known for his work with hard rock band Thunder and melodic rock band Magnum.\n\nThe Wombats: The Wombats are an English rock band formed in Liverpool in 2003.  The band is composed of lead vocalist and guitarist Matthew Murphy, drummer Dan Haggis, and bassist Tord Øverland Knudsen, and has been since its inception.  The band is signed to 14th Floor Records in the United Kingdom and Bright Antenna in the United States.  The Wombats' albums have sold over 1 million copies worldwide.\n\nKing Crimson: King Crimson are an English rock band formed in London in 1968.  The band has undergone numerous formations throughout its history of which 21 musicians have been members; since January 2017 it has consisted of Robert Fripp, Jakko Jakszyk, Tony Levin, Mel Collins, Pat Mastelotto, Gavin Harrison, Bill Rieflin and Jeremy Stacey.  Fripp is the only consistent member of the group, and is considered the band's leader and driving force.  The band has earned a large cult following.  They were ranked No. 87 on VH1's \"100 Greatest Artists of Hard Rock\".\n\nE. F. Band: E.F. Band was a Swedish band that sometimes were mixed up with the New wave of British heavy metal movement, even though they were Swedish.  The band was formed in 1978 by bassist/vocalist Pär Ericsson and guitarist Bengt Fischer, two former members of the progressive rock band Epizootic, who were initially joined by Tommy Lager on drums.  The \"E.F.\" portion of the band's name was derived from the first letter of Ericsson and Fischer's last names.  After recording their first (split) single, the band hired British drummer Dave Dufort, who had played with Mike Oldfield and Screaming Lord Sutch to solidify the line-up.\n\nNorman &quot;Dinky&quot; Diamond: Norman Victor \"Dinky\" Diamond (15 December 1950–10 September 2004) was a British drummer who played with the rock band Sparks at the height of their fame in the UK in the early 1970s, playing on the albums \"Kimono My House\" (1974), \"Propaganda\" (1974) and \"Indiscreet\" (1975).  In 1975 Diamond was voted Drummer of the Year in a poll held by Premier Drums.  He committed suicide by hanging in 2004 after a long-running dispute with noisy neighbours.\n\nSilver Liner: Silver Liner is the third studio album by English multi-instrumentalist and record producer Ethan Johns, released on November 27, 2015 on Johns' own label, Three Crows Records.  Produced by drummer Jeremy Stacey, Johns was accompanied on the album by The Black Eyed Dogs; a backing band includeding Stacey, pedal steel guitarist B. J. Cole and bass guitarist Nick Pini.\n\nEcho &amp; the Bunnymen: Echo & the Bunnymen are an English rock band formed in Liverpool in 1978.  The original line-up consisted of vocalist Ian McCulloch, guitarist Will Sergeant and bassist Les Pattinson, supplemented by a drum machine.  By 1980, Pete de Freitas joined as the band's drummer.\n\nAlan White (Oasis drummer): Alan Victor White (born 26 May 1972 in Lewisham, South London) is an English rock drummer, best known as being the drummer of the English rock band Oasis from 1995 to 2004.  Before Oasis, he was the drummer of Starclub from 1991 to 1994.  He is the longest serving drummer in the band's history, performing on four studio albums, two compilation albums and one live album during his tenure.  He joined the band in May 1995 after the band's original drummer Tony McCarroll was removed from the band.  He was recommended to Noel Gallagher by Gallagher's friend Paul Weller.  Notably, Alan's brother Steve has been longtime drummer for Weller.  White left Oasis in early 2004 in somewhat unclear circumstances.  He was replaced by Zak Starkey, drummer of The Who and son of The Beatles' drummer Ringo Starr.\n\nThe Lemon Trees: The Lemon Trees were a 1990s UK pop band consisting of Guy Chambers, twin brothers Paul Stacey and Jeremy Stacey, Alex Lewis and Paul Holman.  The band formed in 1993 and recorded two albums, but the second was not released.  They disbanded in 1995.\n\nJeremy Stacey: Jeremy Stacey (born September 27, 1963) is a British drummer.  His early work included the 1990s band, The Lemon Trees (with twin brother Paul Stacey on guitars, Guy Chambers and others) and Denzil.  He has also played with Sheryl Crow, the Finn Brothers, Nick Harper, Noel Gallagher, The Waterboys, Thomas Anders, Echo & the Bunnymen, Eurythmics, Joe Cocker, Chris Robinson of the Black Crowes, Adam F, Andrea Bocelli, Patricia Kaas, Susanna Hoffs, Mike Scott, Robbie Williams, Aztec Camera, Charlotte Gainsbourg, Nerina Pallot, Claire Martin (drums on \"Take 1My Heart\", 1999), Mark Wingfield, Iain Ballamy, Chris Squire (\"Chris Squire's Swiss Choir\"), The Syn (\"Syndestructible\", 2005, again with Paul Stacey), Sia Furler (\"Colour the Small One\"), Laurence Cottle, Jason Rebello, Zero 7, Malcolm McLaren, Boris Grebenshikov and Steve Hackett.\n\nQuestion: Jeremy Stacey is a British drummer who played with an English rock band formed in Liverpool in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"drummer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the drummer.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band the drummer played with.\"\n    },\n    \"band_origin_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the band was formed.\"\n    },\n    \"band_formation_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the band was formed.\"\n    },\n    \"is_english_band\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the band is an English rock band.\"\n    }\n  },\n  \"required\": [\n    \"drummer_name\",\n    \"band_name\",\n    \"band_origin_city\",\n    \"band_formation_year\",\n    \"is_english_band\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "drummer_name": {
        "type": "string",
        "description": "The name of the drummer."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band the drummer played with."
      },
      "band_origin_city": {
        "type": "string",
        "description": "The city where the band was formed."
      },
      "band_formation_year": {
        "type": "integer",
        "description": "The year the band was formed."
      },
      "is_english_band": {
        "type": "boolean",
        "description": "Indicates if the band is an English rock band."
      }
    },
    "required": [
      "drummer_name",
      "band_name",
      "band_origin_city",
      "band_formation_year",
      "is_english_band"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
