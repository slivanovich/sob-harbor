{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSingapore Short Film Awards: The Singapore Short Film Awards (abbreviation: SSFA) is an annual event which promotes and recognises excellence in short films in Singapore.  It began in 2010 and was jointly organised by The Substation and Objectifs, presented by The Substation's Moving Images.  Created by filmmaker Chai Yee Wei, former Programme Manager of The Substation's Moving Images Low Beng Kheng and current Co-Founder of Objectifs Yuni Hadi, the Singapore Short Film Awards highlights quality work done annually in the short film genre in Singapore - by seeking out new talent, reflecting current standards of the short film genre and to bring together both the veterans and the young talents as a community to create a space for networking and sharing.\n\nAutomatic Performance Control: Automatic Performance Control (APC) was the first engine knock and boost control system that was introduced on turbo charged Saab H engines in 1982 and was fitted to all subsequent 900 Turbos through 1993 (and 1994 convertibles), as well as 9000 Turbos through 1989.\n\nHonda Zest: The Honda Zest is a kei car released in 2006 by Honda.  It is mechanically identical to the fifth generation Honda Life.  Equipped with a turbo charged engine, 3 cylinders, and 4 doors, it was the first kei car available with optional side curtain airbags.  It was available in two distinct versions — Zest and Zest Sports.  During fall/winter 2008, the Zest Sports was replaced with the Zest Spark.  Honda enlisted J-Pop mega-star Ayumi Hamasaki to promote the Zest Spark.  The Ayu x ZEST SPARK collaboration has come to the extent where the limited edition of the vehicle features Ayu's \"A\" logo, known as \"A Style Package\".\n\nThe Fast and the Furious: The Fast and the Furious (also known as Fast & Furious) is an American franchise based on a series of action films that is largely concerned with illegal street racing and heists, and includes material in various other media that depicts characters and situations from the films.  Distributed by Universal Pictures, the series was established with the 2001 film titled \"The Fast and the Furious\"; this was followed by seven sequels, two short films that tie into the series, and as of May 2017, it has become Universal's biggest franchise of all time, currently the sixth-highest-grossing film series of all time with a combined gross of over $5 billion.\n\nThe Master (2016 film): The Master is a 2016 computer animated short film directed by Jon Saunders, written by Jon Saunders, Ross Evans, Carey Yost and Remington D. Donovan and produced by Ryan Halprin.  The short film was released on September 23, 2016, with Warner Animation Group's \"Storks\".  It stars Jackie Chan as Master Wu.  The short follows Wu and an annoying chicken.  This is the first Lego short film to be released in theaters, and is also the first theatrical short film from the \"Lego Movie\" franchise.\n\nTurbo Charged Prelude: The Turbo Charged Prelude for 2 Fast 2 Furious is a 2003 American short film directed by Philip G. Atwell, produced by Chris Palladino, and written by Keith Dinielli.  It is the second installment in \"The Fast and the Furious\" franchise, and stars Paul Walker.  \"Turbo Charged Prelude\" is a continuation to \"The Fast and the Furious\" (2001) and details the events prior to \"2 Fast 2 Furious\" (2003), where runaway fugitive Brian O'Connor leaves Los Angeles in order to evade police capture.\n\nVetter Mystery Ship: The Mystery Ship was a limited edition motorcycle created by Craig Vetter and released in 1980.  Only 10 were built, of which seven were sold.  An example is on display at the AMA Motorcycle Museum in Ohio, and another at Barber Vintage Motorsports Museum in Leeds, Al.  The one on display at the Barber museum is #9 and is a Turbo charged model.\n\nPrelude to Axanar: Prelude to Axanar (working title: \"Star Trek: Prelude to Axanar\", and long title: \"The Four Years War Part III: Prelude to Axanar\") is a 2014 American fan made short film, directed by Christian Gossett and written by Christian Gossett and Alec Peters.  Funded through Kickstarter, production sought $10,000 in funding, but raised $101,000.  It had its public debut July 26, 2014 at the San Diego Comic-Con.\n\nOh Lucy! (2014 film): Oh Lucy!  is a short film directed by Atsuko Hirayanagi.  The short film made its world premiere at the 2014 Cannes Film Festival receiving 2nd place in the Cinéfondation.  Oh Lucy!  has since become Academy Qualified by winning the Best International Short Film Award at the 2015 Flickerfest as well as the Short Film Jury Award: International Fiction at the 2015 Sundance Film Festival.  The short film is the basis of an upcoming eponymous film adaption, also directed by Hirayanagi.\n\nAfrica, Prelude to Victory: Africa, Prelude to Victory was a short dramatic propaganda film produced by the Office of War Information (OWI) in the 1942 Frank Capra's film \"Prelude to War\".  It shows the african campaigns of World War II.  It was nominated for an Academy Award for Best Documentary in 1943.\n\nQuestion: Who distributed the short film \"Turbo Charged Prelude\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the short film.\"\n    },\n    \"distributor\": {\n      \"type\": \"string\",\n      \"description\": \"The company that distributed the film.\"\n    },\n    \"is_part_of_franchise\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is part of a larger franchise.\"\n    },\n    \"franchise_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the franchise the film belongs to.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"distributor\",\n    \"is_part_of_franchise\",\n    \"franchise_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the short film."
      },
      "distributor": {
        "type": "string",
        "description": "The company that distributed the film."
      },
      "is_part_of_franchise": {
        "type": "boolean",
        "description": "Indicates if the film is part of a larger franchise."
      },
      "franchise_name": {
        "type": "string",
        "description": "The name of the franchise the film belongs to."
      }
    },
    "required": [
      "film_title",
      "distributor",
      "is_part_of_franchise",
      "franchise_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
