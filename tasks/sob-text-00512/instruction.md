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
Gandhigiri (film): Gandhigiri (Hindi: गांधीगीरी) is a 2016 Bollywood film starring Om Puri, Sanjay Mishra, Brijesh Karniwal, Anupam Shyam, Mukesh Tiwari, Dolly Chawla, Meghna Haldar, Rishi Bhutani, Ravi Singh and Ram Sujan Singh.  The movie is directed by Sanoj Mishra, and produced by Aagaman films Pvt. Ltd. of Sudhir Jain & Pratap Singh Yadav.

Anita and Me (film): Anita and Me is a British comedy-drama film released in 2002 based on the book of the same name by Meera Syal.  It was released during a period of popularity for British Asian films, alongside such as "East Is East" and "Bend It Like Beckham".

Rambhajjan Zindabaad: Rambhajjan Zindabaad (English: "Rise Of Rama Song" ) is a Bollywood fiction film produced by Khalid Kidwai, starring Om Puri in the lead role

East Is East (1999 film): East Is East is a 1999 British comedy-drama film written by Ayub Khan-Din and directed by Damien O'Donnell.  It is set in Salford, Lancashire, in 1971, in a mixed-ethnicity British household headed by Pakistani father George (Om Puri) and an English mother, Ella (Linda Bassett).

Current (1992 film): Current is 14 Feb 1992 Indian drama film.  The film was co-written and directed by K. Hariharan, in his Hindi cinema debut, for the National Film Development Corporation of India.  Starring Om Puri and Deepti Naval in the lead, the film focussed about the plight of a farmer in rural India.

Ansh: The Deadly Part: This story is about Deputy Superintendent of Police Bhagat Pandey (Om Puri), who is thorough, honest, and has an excellent track record of apprehending criminals.This story is about Deputy Superintendent of Police Bhagat Pandey (Om Puri), who is thorough, honest, and has an excellent track record of apprehending criminals.  This background creates problems for him with other criminals who are closely connected to powerful politicians.  As a result he is transferred to Bombay (now known as Mumbai).  He takes charge of his post, and transforms everything to a diligent and honest policing machine.  Unfortunately, politicians and criminals alike do not like his diligence, and talk about transferring him to Kashmir, where he will be killed in an encounter by a terrorist.  Bhagat also comes in touch with suspended Police Inspector Sukhdev Singh, and gangleader, Rajnath Guru, the son of a freedom-fighter, Dinanathji (Aloknath).  A truly moving movie depicting characters from India's freedom struggle against the British, Raj Guru, Bhagat Singh, and Sukhdev Singh were the ones who fought for freedom again the British, in this kalyuga, the three Rajnath Guru, Bhagat Pandey, and Sukhdev Singh must fight against corruption and their very own lives.

Yamini Singh: Yamini Singh (born 20 March 1971) is an Indian film and television actress who works in Bollywood films and television.  Her first film role came in K. Bikram Singh's Tarpan (1994), also starring Om Puri, Revathi, Manohar Singh and Mita Vashisht.  Some of her television shows are: Bandhan (1999), Daaman (2001), Chalti Ka Naam Gaadi...Let's Go (2015), Mere Ghar Aayi Ek Nanhi Pari (2009), Har Ghar Kuch Kehta Hai (2007) and Jhoome Jiiya Re (2007).

Tarpan (film): Tarpan (English title: The Absolution) was a 1994 Indian Hindi drama film written and directed by K. Bikram Singh, and starring Om Puri, Revathy, Dina Pathak, Manohar Singh and Mita Vashisht in lead roles.  This directorial debut film was jointly produced by NFDC and Doordarshan.  The film set in the 1940s, in a fictitious village in the Shekhavati region in Rajasthan, where no girl child survives beyond the age of seven.  It deals with larger issues of communalism and caste system through four inter-related stories.

Antaral: Antaral (translation: gap in time, interval) is a television series broadcast on Star TV in 2000, starring Om Puri, Aamir Bashir, Arundhati, Joy Sengupta, Uttara Baokar and others.

King of Bollywood: King of Bollywood is a 2004 Bollywood comedy film directed by Piyush Jha and starring Om Puri.  The film is a satire of the Hindi film industry.

Question: Who wrote the Salford-set 1999 British comedy starring Om Puri that rose to popularity along with Anita and Me?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_nationality": {
      "type": "string",
      "description": "The nationality of the film (e.g., British, Indian)."
    },
    "film_setting_city": {
      "type": "string",
      "description": "The city where the film is set."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "lead_actor": {
      "type": "string",
      "description": "The name of the lead actor in the film."
    },
    "writer_name": {
      "type": "string",
      "description": "The name of the person who wrote the film."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_nationality",
    "film_setting_city",
    "film_genre",
    "lead_actor",
    "writer_name"
  ],
  "additionalProperties": false
}
