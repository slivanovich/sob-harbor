{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGerard Way: Gerard Arthur Way (born April 9, 1977) is an American singer, songwriter, musician, and comic book writer who was the lead vocalist and co-founder of the rock band My Chemical Romance from its formation in September 2001 until its split in March 2013.  His debut solo album \"Hesitant Alien\" was released on September 30, 2014.  He also wrote the comic mini-series \"The True Lives of the Fabulous Killjoys\" and the Eisner Award-winning comic book \"The Umbrella Academy\".\n\nSha Sha: Sha Sha is the debut album by American indie rock singer, songwriter, multi-instrumentalist and former Radish member Ben Kweller.  The album was originally composed of outtakes from sessions for Radish's unreleased album \"Discount Fireworks.\"  It was self-released by Kweller, via CD-R, in 2000.  In 2002, ATO Records released a second version of the album with a radically different track listing featuring many new recordings and songs.\n\nThe Noise Company: The Noise Company is an American independent record label based in Austin, TX.  The label was founded in 2007 by recording artist Ben Kweller.  So far, The Noise Co. has 2 releases to its name: How Ya Lookin' Southbound?  Come In... and Changing Horses.  Both of these were co-released with Kweller's long-time label-home, ATO Records.  Kweller stated in an Australian magazine that he has recently parted ways with ATO and plans to release his upcoming LP solely on The Noise Co.  Kweller stated that he is not interested in signing other artists to the label at this time, but that it is a \"long-term goal\".  The Noise Company LLC was incorporated on January 22, 2011.\n\nChanging Horses (Ben Kweller album): Changing Horses is the fourth studio album by Ben Kweller, which was expected for release in September 2008 but was eventually released on February 2, 2009 in Europe and February 3 2009 in the United States.  Kweller has described the new album as being more Country in style than his previous releases.  The album features his rhythm section Chris Morrissey (bass) and Mark Stepro (drums).  It also debuts the talents of Kitt Kitterman, Kweller's manager, who plays pedal steel guitar and Dobro.  On November 23, 2008, the full album leaked onto the Internet.  In a statement, ATO Records said the leak was not the final version of the album.  The song \"Hurtin' You\" was debuted on Stereogum.  The whole album was made available to stream exclusively on Last.fm.\n\nFreak Out, It's Ben Kweller: Freak Out, It's Ben Kweller is Ben Kweller's self-released demo.  Ben recorded the tracks on his computer in his apartment in Brooklyn.\n\nCaptain Underpants: The First Epic Movie: Captain Underpants: The First Epic Movie is a 2017 American computer-animated comedy film based on the children's novel series of the same name by Dav Pilkey.  It was produced by DreamWorks Animation and Scholastic Entertainment, with animation production provided by Mikros Image Montreal.  It was directed by David Soren from a screenplay by Nicholas Stoller, and stars the voices of Kevin Hart, Ed Helms, Thomas Middleditch, Nick Kroll, Jordan Peele, and Kristen Schaal.  The plot follows two imaginative elementary school pranksters named George Beard and Harold Hutchins (Hart and Middleditch) who hypnotize their mean-spirited principal, Mr. Krupp (Helms), into thinking he is Captain Underpants, a superhero who fights crime while wearing only underwear and a cape who George and Harold write comic books about.\n\nRoger Greenawalt: Roger McEvoy Greenawalt is a music producer and musician known for carrying a ukulele at all times everywhere he goes.  Greenawalt has worked with Iggy Pop, Rufus Wainwright, Nils Lofgren, The Pierces, Ben Kweller, Ric Ocasek, Branford Marsalis, Joe Strummer, Philip Glass and many others.  A story on Greenawalt's discovery of Kweller appeared in the New Yorker on April 7, 1997. [1] Greenawalt is currently focusing on his multimedia project incorporating poetry, music and photography entitled 366 Visions.\n\nOn My Way (Ben Kweller album): On My Way is the second album released by Ben Kweller.  All songs were written by Ben Kweller.\n\nBen Kweller (album): Ben Kweller is the self-titled third album by Ben Kweller.  It was released September 19, 2006 on ATO Records.\n\nBen Kweller: Benjamin Lev \"Ben\" Kweller (born June 16, 1981) is an American singer, songwriter and multi-instrumentalist.\n\nQuestion: Do both Gerard Way and Ben Kweller write comic books?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"gerard_way_writes_comics\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if Gerard Way is stated to write comic books in the context, false otherwise.\"\n    },\n    \"ben_kweller_writes_comics\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if Ben Kweller is stated to write comic books in the context, false otherwise.\"\n    },\n    \"comic_books_by_gerard_way\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of comic books written by Gerard Way mentioned in the context.\"\n    },\n    \"both_write_comics\": {\n      \"type\": \"boolean\",\n      \"description\": \"The final answer to whether both individuals write comic books.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"gerard_way_writes_comics\",\n    \"ben_kweller_writes_comics\",\n    \"comic_books_by_gerard_way\",\n    \"both_write_comics\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "gerard_way_writes_comics": {
        "type": "boolean",
        "description": "True if Gerard Way is stated to write comic books in the context, false otherwise."
      },
      "ben_kweller_writes_comics": {
        "type": "boolean",
        "description": "True if Ben Kweller is stated to write comic books in the context, false otherwise."
      },
      "comic_books_by_gerard_way": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of comic books written by Gerard Way mentioned in the context."
      },
      "both_write_comics": {
        "type": "boolean",
        "description": "The final answer to whether both individuals write comic books."
      }
    },
    "required": [
      "question_asked",
      "gerard_way_writes_comics",
      "ben_kweller_writes_comics",
      "comic_books_by_gerard_way",
      "both_write_comics"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
