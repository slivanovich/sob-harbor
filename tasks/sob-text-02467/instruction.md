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
Ghantasala (singer): Ghantasala Venkateswara Rao (4 December 1922 – 11 February 1974) was an Indian film, composer, playback singer known for his works predominantly in Telugu cinema, and a few Tamil, Kannada, Malayalam, Tulu and Hindi language films.  In 1970, he received the Padma Shri award, India's fourth highest civilian award for his contribution to Indian cinema.  According to "The Hindu" and "The Indian Express", Ghantasala was "Such a divine talent and with his songs he could move the hearts of the people."  "Ghantasala's blending of classical improvisations to the art of light music combined with his virtuosity and sensitivity puts him a class apart, above all others in the field of playback singing"."  "Gifted with what Indian Film Historian V. A. K. Ranga Rao called "the most majestic voice", Ghantasala helped Telugu film music develop its own distinct character which remains unparalleled".  He is referred to as the "Gaana Gandharva" for his mesmerising voice and musical skills.

Mehmood Ali (producer): Mehmood Ali (born 5 July 1971, Mumbai, India) is an Indian film producer, director, writer and distributor.  Started his career as writer with his mentor veteran actor director Kadar Khan shaab.  He is now well known producer and director in Indian Film Industry.  In 2004 he launched his own company Pen N Camera International which is now one of the leading distribution house in Indian Film Industry.

Indian Film Festival of Melbourne: The Indian Film Festival of Melbourne (IFFM) is an annual Indian film festival based in Melbourne, Australia.  It is presented by Film Victoria and the State Government of Victoria, and produced by "Mind Blowing Films", a Melbourne-based distributor of Indian cinema across Australia and New Zealand.  Founded in 2010, the festival was previously called Bollywood & Beyond, and from 2012 was re-established as an initiative of the Victorian Coalition Government Victorian Government that aims to strengthen ties between the Indian film industry and Victoria.  Award-winning Bollywood actress, Vidya Balan is the ambassador for the Indian Film Festival Melbourne, and has been since its initiation.  IFFM is an important fixture in the local arts calendar: permitting a local audience to engage with some of Bollywood's best.  The festival also travels to Sydney, and has previously travelled to Adelaide, Perth and Auckland.The festival presents a diverse array of film and events: with cinema: both indie and Bollywood, curated from across both India and the diaspora, and strives to foster an inclusive cultural collaboration.

Poovarasam Peepee: Poovarasam Peepee (English: "Whistle made from the leave(s) of the Poovarasu Tree" ) is a 2014 Indian children's adventure film directed and written by Halitha Shameem, in her directorial debut.  The film, produced and filmed by Manoj Paramahamsa, revolves around three boys—played by Gaurav Kalai, Pravin Kishore and Vasanth—and their summertime adventures.  It features music by Aruldev.  Distributed by SPI Cinemas, it was released on 30 May 2014.

Thespesia populnea: Thespesia populnea, commonly known as the Indian tulip tree, Pacific rosewood, or Portia tree , is species of flowering plant in the mallow family, Malvaceae.  It is a small tree or arborescent shrub that has a pantropical distribution, found on coasts around the world.  However, the Portia tree is probably native only to the Old World, and may have originated in India.  Nowadays, its wood is mainly used in making furniture because of its good ability to undergo carving.  The wood from the tree was used by early Tamil people to make instruments in ancient Tamilakam.  It is possibly indigenous to the Hawaiian Islands and elsewhere in the Pacific, but may have been spread by early Polynesians for its useful wood and bast fibres.  The Portia tree reaches a height of 6 - tall and a trunk diameter of 20 - .  It grows at elevations from sea level to 275 m in areas that receive 500 - of annual rainfall.  The Portia tree is able to grow in the wide range of soil types that may be present in coastal environments, including soils derived from quartz (sand), limestone, and basalt; it favours neutral soils (pH of 6–7.4).

5th IIFA Awards: The 2004 IIFA Awards, officially known as the 5th International Indian Film Academy Awards ceremony, presented by the International Indian Film Academy honoured the best films of 2003 and took place between May 20–22, 2004.  This year, the city of Singapore played host to the Indian Film Industry.  The tag line of this year's IIFA Awards was "Uniquely IIFA, Uniquely Singapore ...".

Judhajit Bagchi: Judhajit Bagchi, also known as Jeet (born 26 October 1981) is an Indian film director, screenwriter, editor and producer.  Bagchi works with Ranadeep Bhattacharyya and together, they directed and produced the film "Amen" (2010).  In both 2015 and 2016, Bagchi won the International Business Award (Stevie Award) and the Cannes Corporate media and TV award.  He was the first Indian film maker to win these awards and the only Indian film maker to win them in consecutive years.

2nd IIFA Awards: The 2001 IIFA Awards, officially known as the 2nd International Indian Film Academy Awards ceremony, presented by the International Indian Film Academy honoured the best films of 2000 and took place between June16, 2001.  This year, the city of Sun City played host to the Indian Film Industry.

1000 Crore Club: 1000 Crore Club is an unofficial designation by the Indian film trade and the media, related to Indian language films that have grossed ₹1000 crore (10 billion Indian rupees) or more worldwide.  It emerged in May 2017, when two Indian films crossed the () milestone.  The South Indian film "" became the first Indian film to gross over 1000 crore worldwide.  It was followed by the Aamir Khan starring Bollywood film "Dangal", which is the highest grossing Indian film, expanding the club to 1700 crore, 1800 crore and 1900 crore, before creating the () club.  "Dangal" became the fifth highest-grossing non-English language film of all time, with its global ticket sales exceeding $311 million.

Manna Mohie: Manna Mohie also known as "Manpreet Singh" (born 24 January 1968, Punjab, India) is an Indian film producer and Actor.  Started his career as Actor/Producer with his debut Feature Film Welcome M1LL10NS.  He is now well known producer in Indian Film Industry.  In 2016 he launched his own company "Manna Mohie Films" signing up Director from Indian Film Industry Milroy Goes.

Question: What is a tree that could have been featured in the Indian film Poovarasam Peepee?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the Indian film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "tree_reference_in_title": {
          "type": "string",
          "description": "The name of the tree explicitly referenced in the film's title translation."
        }
      },
      "required": [
        "title",
        "release_year",
        "tree_reference_in_title"
      ],
      "additionalProperties": false
    },
    "tree_details": {
      "type": "object",
      "properties": {
        "scientific_name": {
          "type": "string",
          "description": "The scientific name of the tree."
        },
        "common_names": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other common names for the tree."
        },
        "native_region_hint": {
          "type": "string",
          "description": "Information about the tree's probable native region."
        }
      },
      "required": [
        "scientific_name",
        "common_names",
        "native_region_hint"
      ],
      "additionalProperties": false
    },
    "reasoning_for_connection": {
      "type": "string",
      "description": "Explanation of why this specific tree could be featured in the film based on the context."
    }
  },
  "required": [
    "film_details",
    "tree_details",
    "reasoning_for_connection"
  ],
  "additionalProperties": false
}
