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
Alyson Cambridge: Alyson Cambridge is an American operatic soprano.  A native of Washington D.C., she attended school in Cambridge and Oberlin College and studied at the Curtis Institute of Music.  In 2003 she won the Metropolitan Opera National Council Auditions, which gained her entrance into the Metropolitan Opera's Lindemann Young Artist Development Program.  In 2004 she made her Met debut as Frasquita in Georges Bizet's "Carmen".  She has since appeared in several roles with that company, including Giannetta in "L'elisir d'amore", a Flower Maiden in "Parsifal", Karolka in "Jenůfa", Crobyle in "Thaïs", and Bianca in "La Rondine".

Paris Opera: The Paris Opera (French: "Opéra de Paris" ;    ) is the primary opera company of France.  It was founded in 1669 by Louis XIV as the Académie d'Opéra , and shortly thereafter was placed under the leadership of Jean-Baptiste Lully and officially renamed the Académie Royale de Musique , but continued to be known more simply as the Opéra .  Classical ballet as we know it today arose within the Paris Opera as the Paris Opera Ballet and has remained an integral and important part of the company.  Currently called the Opéra National de Paris , it mainly produces operas at its modern 2700-seat theatre Opéra Bastille which opened in 1989, and ballets and some classical operas at the older 1970-seat Palais Garnier which opened in 1875.  Small scale and contemporary works are also staged in the 500-seat Amphitheatre under the Opéra Bastille.

Théâtre Édouard VII: The Théâtre Édouard VII, also called théâtre Édouard VII – Sacha Guitry, is located in Paris between the Madeleine and the Opéra Garnier in the 9th arrondissement.  The square, in which there is a statue of King Edward the seventh, was opened in 1911.  The theatre, which was originally a cinema, was named in the honour of King Edward 7, as he was nicknamed the "most Parisian of all Kings", appreciative of French culture.  In the early to mid 1900s,under the direction of Sacha Guitry, the theatre became a symbol of anglo-franco friendship, and where French people could discover and enjoy Anglo Saxon works.  French actor and director Bernard Murat is the current director of the theatre.  Modern "boulevard comedies" and vaudevilles are often performed there, and subtitled in English by the company Theatre in Paris.  Important figures in the arts, cinema and theatre have performed there, including Orson Welles, Eartha Kitt, and more.  Pablo Picasso created props for a play at the Théâtre Edouard VII in 1944.

Palais Garnier: The Palais Garnier (] French    ) is a 1,979-seat opera house, which was built from 1861 to 1875 for the Paris Opera.  It was called the Salle des Capucines, because of its location on the Boulevard des Capucines in the 9th arrondissement of Paris, but soon became known as the Palais Garnier, in recognition of its opulence and its architect, Charles Garnier.  The theatre is also often referred to as the Opéra Garnier (French    ) and historically was known as the Opéra de Paris or simply the Opéra, as it was the primary home of the Paris Opera and its associated Paris Opera Ballet until 1989, when the Opéra Bastille opened at the Place de la Bastille.  The Paris Opera now mainly uses the Palais Garnier for ballet.

Méditation (Thaïs): "Méditation" (] ) is a symphonic intermezzo from the opera "Thaïs" by French composer Jules Massenet.  The piece is written for solo violin and orchestra.  The opera premiered at the Opéra Garnier in Paris on March 16, 1894.

Rue de la Paix, Paris: The rue de la Paix (] ) is a fashionable shopping street in the center of Paris.  Located in the 2nd arrondissement of Paris, running north from Place Vendôme and ending at the Opéra Garnier, it is best known for its jewellers, such as the shop opened by Cartier in 1898.  Charles Frederick Worth was the first to open a couture house in the rue de la Paix.  Many buildings on the street are inspired in design by the hôtels particuliers of Place Vendôme.

Place de l'Opéra: The Place de l'Opéra is a square in the 9th arrondissement of Paris, at the junction of boulevard des Italiens, boulevard des Capucines, avenue de l'Opéra, rue Auber, rue Halévy, rue de la Paix and rue du Quatre-Septembre.  It was built at the same time as the Opéra Garnier (designed by Charles Garnier), which is sited on it and after which it is named.  Both structures were part of the Haussmannian redesign of Paris under Napoleon III of France.

Thaïs (opera): Thaïs (] ) is an opera, a "comédie lyrique" in three acts and seven tableaux, by Jules Massenet to a French libretto by Louis Gallet, based on the novel "Thaïs" by Anatole France.  It was first performed at the Opéra Garnier in Paris on 16 March 1894, starring the American soprano Sibyl Sanderson, for whom Massenet had written the title role.  The original production was directed by Alexandre Lapissida, with costumes designed by Charles Bianchini and sets by Marcel Jambon (act 1, scene 1; act 3) and Eugène Carpezat (act 1, scene 2; act 2).  The opera was later revised by the composer and was premiered at the same opera house on 13 April 1898.

Le portrait de Manon: The opera was first performed at the Opéra Comique in Paris on 8 May 1894.  After its premiere the work was performed at La Monnaie in November 1894 and the Teatro del Fondo in Naples in December 1894.  The work received its United States premiere at the French Opera House in New Orleans in 1895.  It was also produced at The Waldorf-Astoria Hotel on 13 December 1897.  The Opéra Comique revived the opera in 1900 and it was mounted at the Théâtre Lyrique in September 1922, after which the work fell out of the performance repertory.  After a more than 60-year absence from the stage, "Le portrait de Manon" was mounted at La Fenice on 13 April 1985.  Four years later the Opéra de Monte-Carlo staged the work.  The opera was most recently revived by the Glimmerglass Opera in 2005.  In 2014 "kultur.theater.musik" produced the first performance in German (as "") at the 'Sommeroper im Amthof' festival in Feldkirchen, Carinthia, and in other theatres in Lower Austria.

Le jongleur de Notre-Dame: Le jongleur de Notre-Dame is a three-act opera (labelled in the programme as "Miracle in Three Acts") by Jules Massenet to a French libretto by Maurice Léna.  It was first performed at the Opéra Garnier in Monte Carlo on 18 February 1902.

Question: Who appeared as what in several roles with that company, including Giannetta in what was first performed at the Opéra Garnier in Paris on 16 March 1894?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the person."
        },
        "company_of_performance": {
          "type": "string",
          "description": "The opera company with which the person performed several roles."
        },
        "roles_performed": {
          "type": "array",
          "description": "A list of roles performed by the person with the specified company.",
          "items": {
            "type": "object",
            "properties": {
              "role_name": {
                "type": "string",
                "description": "The name of the role."
              },
              "opera_title": {
                "type": "string",
                "description": "The title of the opera in which the role was performed."
              }
            },
            "required": [
              "role_name",
              "opera_title"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "name",
        "profession",
        "company_of_performance",
        "roles_performed"
      ],
      "additionalProperties": false
    },
    "opera_details_from_question_constraint": {
      "type": "object",
      "properties": {
        "opera_title": {
          "type": "string",
          "description": "The title of the opera that premiered on the specified date and venue."
        },
        "premiere_date": {
          "type": "string",
          "format": "date",
          "description": "The date of the opera's first performance."
        },
        "premiere_venue": {
          "type": "string",
          "description": "The venue where the opera first premiered."
        },
        "premiere_location": {
          "type": "string",
          "description": "The city where the opera first premiered."
        }
      },
      "required": [
        "opera_title",
        "premiere_date",
        "premiere_venue",
        "premiere_location"
      ],
      "additionalProperties": false
    },
    "role_in_constrained_opera_by_person": {
      "type": "object",
      "properties": {
        "person_name": {
          "type": "string",
          "description": "The name of the person who performed a role in the constrained opera."
        },
        "role_name": {
          "type": "string",
          "description": "The specific role performed by the person in the constrained opera."
        },
        "opera_title": {
          "type": "string",
          "description": "The title of the opera in which the role was performed, matching the constrained opera."
        }
      },
      "required": [
        "person_name",
        "role_name",
        "opera_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person",
    "opera_details_from_question_constraint",
    "role_in_constrained_opera_by_person"
  ],
  "additionalProperties": false
}
