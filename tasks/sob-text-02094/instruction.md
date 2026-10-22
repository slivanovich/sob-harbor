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
Whitney Able: Whitney Nees Able (born June 2, 1982) is an American actress and model.  She is best known for her roles in "All the Boys Love Mandy Lane" and "Monsters", and has been featured in "Maxim" magazine.

Science fiction films in India: The genre of science fiction has been prevalent in the Indian film industry since the second half of the 20th century.  Beginning in 1952, the film "Kaadu" was made, which was a Tamil-American co-production. " The Alien" was a science fiction film under production in the late 1960s which was eventually cancelled.  The film was being directed by Bengali Indian director Satyajit Ray and produced by Hollywood studio Columbia Pictures.  The script was written by Ray in 1967, based on "Bankubabur Bandhu", a Bengali story he had written in 1962 for "Sandesh", the Ray family magazine.  In 1987, the superhero film "Mr. India" was a huge success which strengthened the hold of sci-fi films in India, especially Bollywood.  "Indiatimes Movies" ranks the movie amongst the "Top 25 Must See Bollywood Films".  "Mr. India" brought the idea of science fiction to the general people in India.  In 2003, the blockbuster film "Koi... Mil Gaya" marked the beginning of the successful Krrish film series, which is the first sci-fi/superhero film series in Indian cinema.  The 2010 Tamil film "Enthiran" starring Rajinikanth and Aishwarya Rai is the most expensive and most successful sci/fi film ever produced in India.

Boys Love (manga): Boys Love (ボーイズ ラブ ) is a Japanese manga written and illustrated by Kaim Tachibana.  It is licensed in North America by Digital Manga Publishing, which released the first volume through its imprint DokiDoki, on September 23, 2009.  It is licensed in Germany by Egmont Manga & Anime and Taiwan by Ching Win Publishing.  The story is based on the 2006 film "Boys Love" and the follow up 2007 film "Boys Love, the Movie" both co-written directed by Kotaro Terauchi.

Superman Returns: Superman Returns is a 2006 American superhero film directed and produced by Bryan Singer.  It is based on the DC Comics character Superman and serves as an homage sequel to the motion pictures "Superman" (1978) and "Superman II" (1980), while ignoring the events of "Superman III" (1983) and "" (1987).  The film stars Brandon Routh as Clark Kent/Superman, Kate Bosworth as Lois Lane, Kevin Spacey as Lex Luthor, with James Marsden, Frank Langella, and Parker Posey.  The film tells the story of the title character returning to Earth after a five-year absence.  He finds that his love interest Lois Lane has moved on with her life, and that his archenemy Lex Luthor is plotting a scheme that will destroy Superman and the world.

Justice League (film): Justice League is an upcoming American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros.  Pictures.  It is intended to be the fifth installment in the DC Extended Universe (DCEU).  The film is directed by Zack Snyder and written by Chris Terrio and Joss Whedon, from a story by Snyder and Terrio, and features an ensemble cast that includes Ben Affleck, Henry Cavill, Gal Gadot, Jason Momoa, Ezra Miller, Ray Fisher, Ciarán Hinds, Amy Adams, Willem Dafoe, Jesse Eisenberg, Jeremy Irons, Diane Lane, Connie Nielsen, and J. K. Simmons.  In "Justice League", Batman and Wonder Woman assemble a team consisting of Flash, Aquaman, and Cyborg to face the catastrophic threat of Steppenwolf and his army of Parademons.

Supergirl (film): Supergirl is a 1984 British superhero film directed by Jeannot Szwarc and written by David Odell, based on the DC Comics character of the same name and serves as a spin-off to Alexander and Ilya Salkind's "Superman" film series.  The film stars Helen Slater as Supergirl, along with Faye Dunaway, Mia Farrow and Peter O'Toole, with Marc McClure reprising his role as Jimmy Olsen from the "Superman" films.  He was the only actor to do so.  "Supergirl" was the first superhero film to feature a woman in the lead role.

Keith Calder: Keith G. Calder (born December 14, 1979) is a British-born independent film producer best known for his work on "All the Boys Love Mandy Lane" (2006) and "The Wackness" (2008) with Felipe Marino and Joe Neurauter.

All the Boys Love Mandy Lane: All the Boys Love Mandy Lane is a 2006 American horror film directed by Jonathan Levine, and starring Amber Heard, Michael Welch, Whitney Able and Anson Mount.  The plot centers on a group of popular high schoolers who invite an attractive outsider, Mandy Lane, to spend the weekend at a secluded ranch house, where they are followed by a merciless killer.

Amber Heard: Amber Laura Heard (born April 22, 1986) is an American actress.  She made her film debut in 2004 in the sports drama "Friday Night Lights".  After small roles in "North Country" and "Alpha Dog", Heard played her first leading role in "All the Boys Love Mandy Lane" (2006) and appeared in The CW television show "Hidden Palms" (2007).

Aquaman (film): Aquaman is an upcoming American superhero film based on the DC Comics character of the same name, distributed by Warner Bros.  Pictures.  It is intended to be the sixth installment in the DC Extended Universe (DCEU).  The film is being directed by James Wan, with a screenplay by Will Beall, from a story by Wan and Geoff Johns, and stars Jason Momoa, Amber Heard, Patrick Wilson, Willem Dafoe, Yahya Abdul-Mateen II, Temuera Morrison, Dolph Lundgren, and Nicole Kidman.

Question: The star of "All the Boys Love Mandy Lane" appeared in a superhero film directed by this director.

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "star_of_all_the_boys_love_mandy_lane": {
      "type": "string",
      "description": "The actress who starred in 'All the Boys Love Mandy Lane' and also appeared in a superhero film."
    },
    "superhero_film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the superhero film the star appeared in."
        },
        "director": {
          "type": "string",
          "description": "The director of the superhero film."
        }
      },
      "required": [
        "film_title",
        "director"
      ],
      "additionalProperties": false
    },
    "final_answer_director": {
      "type": "string",
      "description": "The director's name that answers the question."
    }
  },
  "required": [
    "star_of_all_the_boys_love_mandy_lane",
    "superhero_film_details",
    "final_answer_director"
  ],
  "additionalProperties": false
}
