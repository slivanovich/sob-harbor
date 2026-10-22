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
Konga (film): Konga is a 1961 British/American international co-production science fiction horror film directed by John Lemont and starring Michael Gough, Margo Johns and Austin Trevor.  It was shot at Merton Park Studios and in Croydon for Anglo Amalgamated, then distributed in the United States by American International Pictures (AIP) as a double feature with "Master of the World".  Anglo Amalgamated and AIP each provided half the funding for the US$500,000 film with each studio receiving distribution rights in their respective hemispheres.

Howard Hawks filmography: Howard Hawks (1896–1977) was an American film director who made 46 films (including two uncredited) between 1926 and 1970.  He is responsible for classic films in genres ranging from film noir, screwball comedy, crime, science fiction and Western.

Attack of the Puppet People: Attack of the Puppet People (also known as "I Was a Teenage Doll" (working title), "Six Inches Tall" (UK) and "The Fantastic Puppet People") is a 1958 American black-and-white science fiction horror film directed, produced and written by Bert I. Gordon.  It stars John Hoyt as an eccentric doll maker.  It was produced by Alta Vista Productions and distributed by American International Pictures as a double feature with "War of the Colossal Beast".

The Rocky Horror Picture Show: The Rocky Horror Picture Show is a 1975 British-American musical screwball comedy horror film by 20th Century Fox produced by Lou Adler and Michael White and directed by Jim Sharman.  The screenplay was written by Sharman and actor Richard O'Brien, who appears in the film, which is based on the 1973 musical stage production "of the same title", with music, book, and lyrics by O'Brien.  The production is a parody tribute to the science fiction and horror B movies of the 1930s through to the early 1970s.  Along with O'Brien, the film stars Tim Curry, Susan Sarandon, and Barry Bostwick and is narrated by Charles Gray with cast members from the original Royal Court Theatre, Roxy Theatre, and Belasco Theatre productions.

The Time Travelers (1964 film): The Time Travelers (a.k.a. Time Trap) is a 1964 science fiction film directed by B-movie director Ib Melchior.  It stars Preston Foster, Philip Carey, Merry Anders, Steve Franken, John Hoyt and Delores Wells.  The cast also includes superfan Forrest J. Ackerman in one of his many bit roles in science fiction films.  The film inspired the 1966 TV series "The Time Tunnel" as well as the 1967 remake "Journey to the Center of Time".  The plot involves a group of scientists who find their time-viewing screen allows them to travel through time.  American International Pictures released the film as a double feature with "Atragon".

Science Fiction/Double Feature: "Science Fiction/Double Feature" is the opening song to the original 1973 musical stage production, "The Rocky Horror Show" as well as its 1975 film counterpart "The Rocky Horror Picture Show", book, music and lyrics by Richard O'Brien, musical arrangements by Richard Hartley.  The song is reprised at the end of the show, with lyrics that reflect on the final events of the story.

The Invisible Woman (1940 film): The Invisible Woman is an American science fiction comedy film that was released near the end of 1940 by Universal.  It is the third "Invisible Man" film following "The Invisible Man" and "The Invisible Man Returns", which had been released earlier in the year.  It was more of a screwball comedy than other films in the series.

Grindhouse (film): Grindhouse is a 2007 American horror film double feature co-written, produced, and directed by Robert Rodriguez and Quentin Tarantino.  The double feature consists of two feature-length segments, Rodriguez's "Planet Terror" and Tarantino's "Death Proof", and is bookended by fictional trailers for upcoming attractions (though two of the trailers, "Machete" and "Hobo with a Shotgun", have since been made into movies), advertisements, and in-theater announcements.  The film's title derives from the U.S. film industry term "grindhouse", which refers to (now mostly defunct) movie theaters specializing in B movies, often exploitation films, shown in a multiple-feature format.  The film stars Rose McGowan, Freddy Rodriguez, Marley Shelton, Michael Biehn, Jeff Fahey, Josh Brolin, Naveen Andrews, Fergie, Bruce Willis, Kurt Russell, Rosario Dawson, Tracie Thoms, Mary Elizabeth Winstead, and stuntwoman Zoë Bell, who plays herself.

Alvin and the Chipmunks Meet the Wolfman: Alvin and the Chipmunks Meet the Wolfman is a 2000 animated horror musical comedy-themed direct-to-video film, produced by Bagdasarian Productions and Universal Cartoon Studios, distributed by Universal Studios Home Entertainment, and based on characters from "Alvin and the Chipmunks".  It was released on VHS in 2000 and DVD (as a "Monster Pack" with "Alvin and the Chipmunks Meet Frankenstein", "Monster Mash", and four episodes of "Archie's Weird Mysteries") in 2004 by Universal Studios Home Entertainment.  A Scare-riffic Double Feature DVD featuring "Alvin and the Chipmunks Meet Frankenstein" and this film was released on September 4, 2007.  Another Scare-riffic Double Feature DVD featuring "Alvin and the Chipmunks Meet Frankenstein" and this film was re-released on March 11, 2008.

Midnite Movies: Midnite Movies is a line of B movies released first on VHS and later on DVD by MGM Home Entertainment.  The line was begun by MGM in March 2001 following its acquisition of Orion Pictures, which bought out Filmways, the owner of American International Pictures.  AIP had a library of B movies from the 1950s and 1960s that were science fiction, horror, and exploitation films.  The "Midnite Movies" collection is primarily derived from the AIP library (including most of Roger Corman's and Vincent Price's horror movies) but also included Hammer Film Productions, Amicus Productions, United Artists, and Empire International Pictures movies as well.  The DVDs were first released as single films but most later releases would be double features on single double-sided discs.  Sony Pictures Home Entertainment later became owners of the MGM library and continued the "Midnite Movies" line with distributor 20th Century Fox Home Entertainment.  All double feature titles released on the 20th Century Fox label were two-disc packages.  By 2011, no new titles were forthcoming; the previous catalog titles slowly went out of print and the "Midnite Movies" website was taken down.

Question: Who directed a 1975 British-American musical screwball comedy horror film which features the song "Science Fiction/Double Feature"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres the film belongs to."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genres",
    "director_name"
  ],
  "additionalProperties": false
}
