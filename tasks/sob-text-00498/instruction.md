Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Hy Hollinger: Herman "Hy" Hollinger (September 3, 1918 – October 7, 2015) was an American trade journalist and studio publicist.  He covered the entertainment industry for both "Variety" (1953–1960, 1979–1992) and "The Hollywood Reporter" (1992–2008) during a career which spanned seven decades.  Hollinger helped to developed a new system for tracking the overseas box office while working for "Variety's" London bureau.  He later served as the international editor at "The Hollywood Reporter" from 1992 until 2008, when he retired at the age of 90.  Hollinger was considered an expert on the international box office and the sale independent productions directly to foreign film distributors.

Mary Murphy (news personality): Mary Murphy is an American television personality, print journalist and author.  She is an on-air correspondent for "The Insider" and a news producer at "Entertainment Tonight".  Murphy is also a Senior Lecturer at USC Annenberg School for Communication and Journalism.  She is a contributor to the "Los Angeles Times Magazine", "USA Weekend Magazine", the "New York Post" and "The Hollywood Reporter".  Murphy has been on the staff of the "Los Angeles Times" and New York, "Esquire", and "TV Guide" Magazines.

Ray Richmond: Ray Richmond (born October 19, 1957 in Whittier, California) is a globally syndicated critic and entertainment/media columnist.  Richmond has also worked variously as a feature and entertainment writer, beat reporter and TV critic for a variety of publications including the "Los Angeles Daily News", "Daily Variety", the "Orange County Register", the late "Los Angeles Herald Examiner", "Deadline Hollywood", "Los Angeles" magazine, "Buzz", "The Hollywood Reporter", the "Los Angeles Times", "New Times Los Angeles", "DGA Magazine", and "Penthouse".

Nylon (magazine): Nylon is an American multi-platform media company and magazine that focus on pop culture and fashion.  Its coverage includes art, beauty, music, design, celebrities, technology and travel.  Its name references New York and London.  Jamie Elden is the President and Chief Revenue Officer and Marc Luzzatto is the chairman and principal owner, and also responsible for the closure of the print magazine.

YoungStar Award: The YoungStar Awards, presented by "The Hollywood Reporter", honored young American actors and actresses from ages 6–18 in their work in film, television, stage and music.  Winners were chosen via a poll of 3,500 entertainment industry insiders who read "The Hollywood Reporter".  The awards ceremony was held from 1995 until 2000; there was no ceremony in 1996.

Animation Magazine: Animation Magazine is an American print magazine and website covering the animation industry and education, as well as visual effects.  The print magazine is published 10 times a year in the United States.

Digital edition: A digital edition is an online magazine or online newspaper delivered in electronic form which is formatted identically to the print version.  Digital editions are often called digital facsimiles to underline the likeness to the print version.  Digital editions have the benefit of reduced cost to the publisher and reader by avoiding the time and expense to print and deliver like a paper edition.  This format is considered more environmentally friendly due to the reduction of paper and energy use.  These editions also often feature interactive elements such as hyperlinks both within the publication itself and to other internet resources, searching and bookmarking, and can also incorporate multimedia such as video or animation to enhance articles themselves or for advertisements.  Some delivery methods also include animation and sound effects replicating page turning to further enhance the experience of their print counterparts.Traditionally, magazine publishers have relied on two revenue sources: selling ads and selling magazines.  Additionally some publishers are using other electronic publication methods such as RSS to reach out to readers and inform them when new digital editions are available.

Coilhouse: Coilhouse was an American digital and print magazine, and corresponding blog.  It was founded in 2007 by Nadya Lev, Meredith Yayanos, and Zoetica Ebb. , and carries the tagline, "A Love Letter to Alternative Culture."  Regular contributors to Coilhouse included Ross Rosenberg, David Forbes, Angeliska Polacheck, and Jeffrey Wengrofsky.

For Your Consideration (advertising): For Your Consideration is a heading frequently used in advertisements in entertainment trade publications such as "Variety, Backstage," and "The Hollywood Reporter".  They are specifically directed towards members of awards voting groups in the entertainment industry, like the Academy of Motion Picture Arts and Sciences that annually presents the Academy Awards celebrating the best in motion pictures, or the Academy of Television Arts & Sciences which presents the Primetime Emmy Awards for television.

The Hollywood Reporter: The Hollywood Reporter (THR) is a multi-platform American digital and print magazine founded in 1930 and focusing on the Hollywood film industry, television, and entertainment industries, as well as Hollywood's intersection with fashion, finance, law, technology, lifestyle, and politics.

Question: For Your Consideration is a heading frequently used in advertisements in the multi-platform American digital and print magazine, The Hollywood Reporter, founded in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "publication_name": {
      "type": "string",
      "description": "The name of the publication."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the publication was founded."
    },
    "publication_formats": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The formats in which the publication is available."
    },
    "advertisement_heading": {
      "type": "string",
      "description": "The specific heading used in advertisements."
    }
  },
  "required": [
    "publication_name",
    "founding_year",
    "publication_formats",
    "advertisement_heading"
  ],
  "additionalProperties": false
}
