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
Sketches of Frank Gehry: Sketches of Frank Gehry is a 2006 American documentary film directed by Sydney Pollack and produced by Ultan Guilfoyle, about the life and work of the Canadian-American architect Frank Gehry.  The film was screened out of competition at the 2006 Cannes Film Festival.  Pollack and Gehry had been friends and mutual admirers for years.  The film features footage of various Gehry-designed buildings, including Anaheim Ice (the training rink of the Mighty Ducks of Anaheim), the Guggenheim Museum Bilbao, and the Walt Disney Concert Hall.  It was the final film to be directed by Sydney Pollack before his death in 2008.

Castle Keep: Castle Keep is a "firmly pro- and anti-war" 1969 American Technicolor war film combining surrealism with tragic realism filmed in Panavision.  It was directed by Sydney Pollack and starred Burt Lancaster, Patrick O'Neal, Jean-Pierre Aumont, Bruce Dern, and Peter Falk.  The movie appeared in the summer of 1969, a few months before the arrival of Pollack's smash hit "They Shoot Horses, Don't They? ".

Three Days of the Condor: Three Days of the Condor (stylized on the poster art as 3 Days of the Condor) is a 1975 American political thriller film directed by Sydney Pollack and starring Robert Redford, Faye Dunaway, Cliff Robertson, and Max von Sydow.  The screenplay by Lorenzo Semple Jr. and David Rayfiel was adapted from the 1974 novel "Six Days of the Condor" by James Grady.  The main point of variance from novel to film lies in the presentation of the CIA.  In Grady's book, a rogue element within the Agency is motivated by drug-running greed.  In the film, the same individuals act with equal ruthlessness to hide a project intended to protect long-term national interests.

Out of Africa (film): Out of Africa is a 1985 American epic romantic drama film directed and produced by Sydney Pollack, and starring Robert Redford and Meryl Streep.  The film is based loosely on the autobiographical book "Out of Africa" written by Isak Dinesen (the pseudonym of Danish author Karen Blixen), which was published in 1937, with additional material from Dinesen's book "Shadows on the Grass" and other sources.  This film received 28 film awards, including seven Academy Awards.

Fredric Steinkamp: Fredric Steinkamp (August 22, 1928 – February 20, 2002) was an American film editor with more than 40 film credits.  He had a longstanding, notable collaboration with director Sydney Pollack, editing nearly all of Pollack's films from "They Shoot Horses, Don't They? " (1969) through "Sabrina" (1995).

Ginny Stikeman: Virginia (Ginny) Stikeman (born 1941) is a Canadian filmmaker.  She has directed, produced and edited many films, with her focus in documentaries.  Her most well-known films are "Sisters in Struggle" (1991), "Dream of a free country: a message from Nicaraguan women" (1983), and "" (1992)

The Yakuza: The Yakuza is a 1974 Japanese-American neo-noir gangster film directed by Sydney Pollack, written by Leonard Schrader, Paul Schrader, and Robert Towne.  The film is about a man (Robert Mitchum) who returns to Japan after several years away in order to rescue his friend's kidnapped daughter.  Following a lackluster initial release, the film has since gained a cult following.

William Steinkamp: William Steinkamp (born June 9, 1953) is an American film editor with more than 20 film credits.  He had a longstanding, notable collaboration with director Sydney Pollack, editing nearly all of Pollack's films from "Tootsie" (1982) through the director's last film, "The Interpreter" (2005).

Sydney Pollack: Sydney Irwin Pollack (July 1, 1934 – May 26, 2008) was an American film director, producer and actor.  Pollack directed more than 20 films and 10 television shows, acted in over 30 films or shows, and produced over 44 films.  His 1985 film "Out of Africa" won him Academy Awards for directing and producing; he was also nominated for Best Director Oscars for "They Shoot Horses, Don't They? " (1969) and "Tootsie" (1982), in the latter of which he also appeared.

Charlie: The Life and Art of Charles Chaplin: Charlie: The Life and Art of Charles Chaplin is a 2003 American biographical documentary film written and directed by film critic Richard Schickel.  The film explores the personal and professional life of the British actor, comedian and filmmaker, Charlie Chaplin, as well as his legacy and influence.  It is narrated by Sydney Pollack along with many Hollywood personalities appearing in the film talking about Chaplin, including Robert Downey Jr., Norman Lloyd, Bill Irwin, Woody Allen, Johnny Depp, Richard Attenborough, Martin Scorsese, Miloš Forman, Marcel Marceau, David Raksin, Claire Bloom, David Thomson, Andrew Sarris, Jeanine Basinger and Chaplin's children Geraldine, Michael and Sydney Chaplin.  The documentary also benefits from insight from key Chaplin biographers David Robinson and Jeffrey Vance.

Question: Sydney Pollack and Ginny Stikeman, are in the industry of film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_in_film_industry": {
      "type": "boolean",
      "description": "True if both individuals are confirmed to be in the film industry, false otherwise."
    },
    "individuals": {
      "type": "array",
      "description": "Details about the individuals mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual."
          },
          "roles": {
            "type": "array",
            "description": "A list of film-related roles held by the individual.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "nationality",
          "roles"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the context."
    }
  },
  "required": [
    "is_in_film_industry",
    "individuals",
    "reasoning"
  ],
  "additionalProperties": false
}
