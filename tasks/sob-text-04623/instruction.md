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
Arthur Penn: Arthur Hiller Penn (September 27, 1922 – September 28, 2010) was an American director and producer of film, television and theater.  Penn directed critically acclaimed films throughout the 1960s such as the drama "The Chase" (1966), the biographical crime film "Bonnie and Clyde" (1967) and the comedy "Alice's Restaurant" (1969).  He also got attention for his revisionist Western "Little Big Man" (1970).

Thirumanassu: Thirumanassu is a 1995 Malayalam film by Aswathi Gopinath starring Saikumar, Charmila, Narendra Prasad, Dileep, K.R. Vijaya and Rajan P. Dev.  The film was originally titled was "Thiruvithamkoor Thirumanassu" which caused controversy and the film makers were forced to change name as Thirumanassu.

Native American Film and Video Festival: The Native American Film and Video Festival is a noncompetitive showcase of film, video and audio productions held biennially in New York City.  Each festival screens between 50 and 80 documentaries, short features and animations, introduced by their producers and members of the native communities represented.  Works to be featured in a given festival are chosen by a team of selectors made up of media makers and cultural activists from among indigenous peoples of the Americas and the program staff of the Film and Video Center of the Smithsonian Institution National Museum of the American Indian.  Selectors have included indigenous film makers such as Chris Eyre, Randy Redroad, and Nora Naranjo-Morse, and Native American cultural experts and academics such as G. Peter Jemison, Beverly Singer, and Paul Apodaca.

Neri (2017 film): Neri is an Indian Tamil-language Comedy Drama written and directed by Bagavathy Bala.  Produced by P.Mohan Kumar under his Amogga Film Makers production company, it stars him in the lead role alongside Shriya Sri.  Production for the film began during Jan 2016.  Film will released on 29 September 2017.

Things That Go Bump In The Night Film Festival: The Things That Go Bump In The Night Film Festival (BUMP FEST) is an annual event in Bay City, Michigan presenting films produced by local film makers.  The films tend to be in the horror, thriller and suspense genres.  The festival is presented by Even Keel Productions and aims to provide a platform for local film makers to showcase their appropriately themed short films.  The current venue for the festival is the Westown Theater in Bay City, Michigan.

FireHollywood: FireHollywood, later named Patriotic Americans Boycotting Anti-American Hollywood (or PABAAH) was a US nationalist-conservative organization that called for the boycott of Hollywood films made by film makers who have made statements deemed by the group to be "unpatriotic," "anti-American" or treasonous.  Though it mainly targeted film makers, it targeted other pop-culture figures, including musicians.

Arthur Cheetham: Arthur Cheetham (1864 – 15 January 1937) was an English-born Welsh filmmaker, who became the first of his profession to be based in Wales.  His legacy is a collection of eight surviving films, including the oldest extant British football 'short' from 1898.  Cheetham, along with fellow cinematic pioneer, William Haggar, are recognised as the only Welsh-based film makers of importance before the First World War.

Penn &amp; Teller Get Killed: Penn & Teller Get Killed is a 1989 black comedy film directed by Arthur Penn starring the magicians Penn & Teller.  The duo play themselves, in a satirical account of what the audience would perhaps imagine the pair doing in their daily lives.  Most of the action involves Penn and Teller playing practical jokes on each other along with Penn's girlfriend, Carlotta (Caitlin Clarke).  The final joke, as the title of the film implies, has serious consequences for all three.  It was the last theatrical film to be directed by Arthur Penn, and received mostly negative reviews from critics.

James P. Hogan (director): James Patrick Hogan (September 21, 1890, Lowell, Massachusetts — November 4, 1943, North Hollywood, California) was an American filmmaker.

M. J. Radhakrishnan: M. J. Radhakrishnan is an award-winning Indian cinematographer working mainly in Malayalam films.  Recently completed his first Telugu film directed by K. N. T. Sastry titled "SHAANU" produced by CFSI (Children's Film Society of India.  He has won Kerala State Award for Best Cinematography 7 times(the most), equaling with Mankada Ravi Varma.  Earlier he worked as a still photographer and then as an associate to renowned cinematographer turned director Shaji N. Karun.  His important works include "Deshadanam", "Karunam" and "Naalu Pennungal".  His films have been screened at several prominent film festivals around the world including Cannes, Toronto, Chicago, Rhode Island and Rotterdam.  One of his works, "Marana Simhasanam" (English: Throne of Death, French: Le Trone de la mort), won Caméra d'Or (Golden Camera Award) in the Un Certain Regard section at the 1999 Cannes Film Festival.  He has worked for over 75 feature films and several documentaries and has worked with some of the prominent Indian film makers including Adoor Gopalakrishnan, Murali Nair, Shaji N. Karun, TV Chandran, Dr. Biju, Jayaraj and Renjith.  He mostly works on arthouse films and is known for his natural lighting styles.In a career spanning more than two decades, he has worked with a number of young film makers, mostly in their maiden ventures.

Question: Film makers Arthur Penn and James P. Hogan are from which nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "filmmakers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the filmmaker."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the filmmaker."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "description": "A list of filmmakers and their nationalities."
    },
    "common_nationality": {
      "type": "string",
      "description": "The nationality shared by all listed filmmakers, if applicable."
    },
    "all_share_nationality": {
      "type": "boolean",
      "description": "True if all listed filmmakers share the same nationality, false otherwise."
    }
  },
  "required": [
    "filmmakers",
    "common_nationality",
    "all_share_nationality"
  ],
  "additionalProperties": false
}
