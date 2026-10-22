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
The Midwich Cuckoos: The Midwich Cuckoos is a science fiction novel written by English author John Wyndham, published during 1957.  It has been filmed twice as "Village of the Damned", with releases during 1960 and 1995.

The Pebble and the Penguin (soundtrack): The Pebble and the Penguin: Original Motion Picture Soundtrack is the 1995 soundtrack to the Don Bluth animated feature film, "The Pebble and the Penguin".  The music for the soundtrack was handled by Barry Manilow, and the lyrics for the songs were all written by Bruce Sussman.  The songs were all arranged and produced by Manilow, and the soundtrack was produced by Manilow and Marc Hulett.  The soundtrack includes various artists with actors singing their parts for the film, including Martin Short, Annie Golden, Tim Curry, and James Belushi among others.  The songs and score for the soundtrack were both performed by the Irish Film Orchestra and the Irish Chamber Choir.  This soundtrack is currently out of print.

Village of the Damned (soundtrack): Village of the Damned is a soundtrack by John Carpenter and Dave Davies for the 1995 film of the same name.  It was released in 1995 through Varèse Sarabande.

John Wyndham: John Wyndham Parkes Lucas Beynon Harris ( ; 10 July 1903 – 11 March 1969) was an English science fiction writer best known for his works written using the pen name John Wyndham, although he also used other combinations of his names, such as John Beynon and Lucas Parkes.  Many of his works were set in post-apocalyptic landscapes.  His best known works include "The Day of the Triffids" (1951) and "The Midwich Cuckoos" (1957), the latter filmed twice as "Village of the Damned".

City of God (2002 film): City of God (Portuguese: "Cidade de Deus" ) is a 2002 Brazilian crime film directed by Fernando Meirelles and co-directed by Kátia Lund, released in its home country in 2002 and worldwide in 2003.  The story was adapted by Bráulio Mantovani from the 1997 novel of the same name written by Paulo Lins, but the plot is loosely based on real events.  It depicts the growth of organized crime in the Cidade de Deus suburb of Rio de Janeiro, between the end of the 1960s and the beginning of the 1980s, with the closure of the film depicting the war between the drug dealer Li'l Zé and vigilante-turned-criminal Knockout Ned.  The tagline is "If you run, the beast catches you; if you stay, the beast eats you", a proverb analogous to the English "Damned if you do, damned if you don't".

Children of the Damned: Children of the Damned is a 1964 British black-and-white science fiction film, a thematic sequel to 1960's "Village of the Damned", which concerns a group of children with similar psi-powers to those in the earlier film.  The film enables a interpretation of the children as being a good and more pure form of human being than evil and alien.

Village of the Damned (1995 film): John Carpenter's Village of the Damned is a 1995 American science fiction-horror film directed by John Carpenter and a remake of the 1960 film of the same name which in turn is based on the novel "The Midwich Cuckoos" by John Wyndham.  The 1995 remake is set in Northern California, whereas the book and original film were both set in the United Kingdom.  The 1995 film was marketed with the tagline, "Beware the Children", and stars Christopher Reeve, Kirstie Alley, Linda Kozlowski, Michael Pare, Mark Hamill, and Meredith Salenger.

The Dead and the Damned 2: The Dead and the Damned 2 (also The Dead, the Damned, and the Darkness and Tom Sawyer vs Zombies) is a 2014 American horror film written and directed by Rene Perez.  It was released direct-to-video on October 7, 2014, and is the sequel to the 2010 film "The Dead and the Damned".

Aaliyah (album): Aaliyah is the third and final studio album by American R&B singer Aaliyah.  After raising her profile with hit soundtrack singles during the late 1990s, the singer started to work on the album in 1998, but rescheduled its recording around her developing film career.  She resumed recording in 2000 at Sing Sing Studios in Australia, where she shot her role for the 2002 film "Queen of the Damned" during the day and recorded songs at night.  Aaliyah worked primarily with Blackground Records' in-house crew of writers and producers, including Bud'da, J. Dub, Rapture, and Eric Seats, as well as longtime collaborator Timbaland.

Beauty and the Beast (1991 soundtrack): Beauty and the Beast: Original Motion Picture Soundtrack is the official soundtrack album to the 1991 Disney animated feature film, "Beauty and the Beast".  Originally released on October 29, 1991, by Walt Disney Records, the album's first half – tracks 2 to 9 – generally contains the film's musical numbers, all of which were written by composer Alan Menken and lyricist Howard Ashman, while its latter half – tracks 10 to 14 – features its musical score, composed solely by Menken.  While the majority of the album's content remains within the musical theatre genre, its songs have also been influenced by French, classical, pop and Broadway music.  Credited to Various Artists, "Beauty and the Beast: Original Motion Picture Soundtrack" features performances by the film's main cast – Paige O'Hara, Richard White, Jesse Corti, Jerry Orbach, Angela Lansbury and Robby Benson – in order of appearance.  Additionally, the album features recording artists Celine Dion and Peabo Bryson, who perform a pop rendition of the film's title and theme song, "Beauty and the Beast", which simultaneously serves as the soundtrack's only single.

Question: What genre is the film that the Village of the Damned soundtrack was written for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film associated with the soundtrack."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "soundtrack_composers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The composers or artists who created the soundtrack."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_genre",
    "soundtrack_composers"
  ],
  "additionalProperties": false
}
