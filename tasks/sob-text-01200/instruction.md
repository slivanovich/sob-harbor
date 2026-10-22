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
Michael Standish: Michael John Standish a British production designer and set decorator.  Best known for his work as set decorator in 2016 "The Danish Girl", which earned him his first Academy Award for Best Production Design nomination at 88th Academy Awards along with British production designer Eve Stewart.

Jan Roelfs: Jan Roelfs (born 1957 in Amsterdam) is a production designer of Dutch descent.  Roelfs was nominated for an Academy Award for Best Art Direction twice for the 1992 film "Orlando" and for the 1997 film "Gattaca".  He shared the "Orlando" nomination with fellow production designer Ben Van Os and the "Gattaca" nomination with set decorator Nancy Nye.  Roelfs also worked as an art director in the 1980s and the 1990s.

Sarah Greenwood: Sarah Greenwood is a production designer.  She has been nominated four times for an Academy Award – in 2006 for "Pride & Prejudice", in 2008 for "Atonement", in 2010 for "Sherlock Holmes" and in 2012 for "Anna Karenina".  In 2013, she was elected best production designer for "Anna Karenina" at the 26th European Film Awards, and won the Art Directors Guild Award for Excellence in Period Film for "Anna Karenina" as well.

Richard III (1995 film): Richard III is a 1995 British drama film adapted from William Shakespeare's play of the same name, starring Ian McKellen, Annette Bening, Jim Broadbent, Robert Downey Jr., Nigel Hawthorne, Kristin Scott Thomas, Maggie Smith, John Wood, and Dominic West.  The film sets the play in a fictional fascist version of 1930s Britain.

Ryo Sugimoto: Ryo Sugimoto Born in 1976.  Sugimoto worked on number of films as an art assistant under Production Designer Mitsuo Harada and Yohei Taneda.  Sugimoto joined NOUVELLE VAGUE Co.,Ltd .  in 2005, has worked on films such as "AEGIS"and "Tokyo Tower" as a set designer and was the art director on "BABEL"(Dir: Alejandro González Iñárritu) which won the Art Excellence in Production Design Award(2006) from the Art Directors Guild.  Sugimoto was the first Production Designer for Junji Sakamoto "Chameleon"(2007), and is the Production designer for "Map of the sounds of Tokyo" directed by Isabel Coixet.  Sugimoto also provides designs for commercials, music videos and interiors,

Tony Burrough: Tony Burrough is a production designer.  He was nominated for an Academy Award in the category Best Art Direction for the film "Richard III".

Nathan Crowley: Nathan Crowley (born 1966) is an English production designer and a former art director.  He was nominated for an Academy Award for Best Production Design for "The Prestige" (2006), "The Dark Knight" (2008), and "Interstellar" (2014).  For "The Prestige", he was nominated with set decorator Julie Ochipinti, for "The Dark Knight", he was nominated with set decorator Peter Lando, and for "Interstellar", he was nominated with set decorator Gary Fettis.  Crowley was also nominated for the BAFTA Award for Best Production Design for "Batman Begins" (2005) and "The Dark Knight" (2008).

Guy Hendrix Dyas: Guy Hendrix Dyas (born 20 August 1968) is a British production designer for feature films.  He collaborated with Christopher Nolan on his science fiction thriller "Inception" which earned him an Academy Award nomination as well as a BAFTA Award for Best Production Design.  In 2017, Dyas was nominated for another Academy Award, this time for his work on Passengers.  In 2010, Dyas became the first British designer to win a Goya Award for Best Production Design for his work on Alejandro Amenábar's historical epic "Agora" which premiered at the 2009 Cannes Film Festival.  Dyas previously received three consecutive Art Directors Guild Award nominations for his production design work on Steven Spielberg's "Indiana Jones and the Kingdom of the Crystal Skull", Shekhar Kapur's "" and "Superman Returns" for Bryan Singer.  He won an ADG award in 2011 for "Inception".  He also earned a BAFTA Award nomination in 2007 for Best Production Design for "Elizabeth: The Golden Age" and for four years in a row Dyas has been named by "The Sunday Times" as one of the top ten Brits working behind the camera in Hollywood.

Adam Stockhausen: Adam Stockhausen is a production designer.  Stockhausen, along with set decorator Anna Pinnock won the Academy Award for Best Production Design for the 2014 film "The Grand Budapest Hotel".  Previously he was nominated for the Academy Award for Best Production Design for the 2013 film "12 Years a Slave" together with set decorator Alice Baker.  He is also nominated for the Academy Award for Best Production Design for the 2015 film "Bridge of Spies" along with set decorators Bernhard Henrich and Rena DeAngelo.

Gene Serdena: Gene Serdena is a set decorator.  Serdena, along with production designer K. K. Barrett, was nominated for an Academy Award for Best Production Design for the 2013 film "Her".  He was nominated again for Best Production Design, alongside production designer Guy Hendrix Dyas, for their work in 2016 film "Passengers at the 89th Academy Awards.

Question: Tony Burrough is a production designer nominated for an Academy Award for a film set  fictional fascist version of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "production_designer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "award_category_nominated_for": {
          "type": "string"
        },
        "setting_description": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "award_category_nominated_for",
        "setting_description"
      ],
      "additionalProperties": false
    },
    "setting_era": {
      "type": "string"
    }
  },
  "required": [
    "production_designer",
    "film_details",
    "setting_era"
  ],
  "additionalProperties": false
}
