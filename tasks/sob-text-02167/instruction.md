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
Ratonero Murciano de Huerta: Murcian Ratter ("Ratonero murciano") or Huerta Ratter ("Ratonero murciano de huerta") is a Spanish breed of dog originating from Murcia.

Small Münsterländer: The Small Münsterländer (also SM or Kleiner Münsterländer) is a versatile hunting-pointing-retrieving dog breed that reached its current form in the area around Münster, Germany.  The Large Münsterländer is from the same area, but was developed from different breeding stock and is not related as the names would suggest.  Small Münsterländers bear a resemblance to both spaniels and setters but are more versatile while hunting on land and water.  The Small Münsterländer is recognized by the Fédération Cynologique Internationale under Group 7, Section 1.2, Continental Pointing Dogs of Spaniel type, by the American Kennel Club as a Foundation Breed, and by The Kennel Club and the United Kennel Club as a gun dog.  It is related to the Epagneul Français and the Drentsche Patrijshond.

Chato Murciano: The Chato Murciano is a breed of domestic pig originating from Murcia, Spain.  It is the only surviving breed of pig locally and historically produced in Murcia and is at the risk of extinction.  Despite its danger of becoming extinct, the Chato Murciano is a well-managed pig known for its production of bacon and lean pork.  Several Spanish authorities specialising in agriculture work on programs aiming to conserve the breed by cross-breeding and artificial insemination

Telomian: The Telomian is a breed of dog native to Malaysia.  Though rare, it remains the only known Malaysian dog breed to live outside its homeland.  Malaysian are used to called this dog breed Anjing Kampung which means Village dog in Malay.  This dog breed is still remained rarest in the world.

Majorca Ratter: Majorca Ratter (Catalan: "Ca Rater Mallorquí"; Spanish: "Ratonero mallorquín") is a Spanish breed of dog originating in the Balearic Islands.

Monastery of Santa María de Huerta: The Monastery of Santa María de Huerta (Spanish: "Monasterio de Santa María de Huerta") is a monastery located in Santa María de Huerta, a small locality of the Spanish Province of Soria, within the autonomous community of Castile and León.  It was declared "Bien de Interés Cultural" in 1882.

List of U.S. state dogs: Twelve states of the United States have designated an official state dog breed.  Maryland was the first state to name a dog breed as a state symbol, naming the Chesapeake Bay Retriever in 1964.  Pennsylvania followed the year after, naming the Great Dane as its official breed.  Dog breeds are mostly affiliated with the states that they originated in.  North Carolina chose the Plott Hound as it was the only dog breed indigenous to the state.

Ratonero Bodeguero Andaluz: The Ratonero Bodeguero Andaluz ("Andalusian wine-cellar rat-hunting dog") is a Spanish breed of dog of the terrier type.  Its name reflects its main occupation: hunting rats and mice hidden between barrels in the wineries of Andalusia in Spain.  It was recognised as an indigenous Spanish breed in 2000 by the Spanish Ministry of Agriculture and by the Spanish Kennel Club, the" Real Sociedad Canina de España".

Drentse Patrijshond: The Drentsche Patrijshond is a versatile spaniel-type hunting dog from the Dutch province of Drenthe.  Called the Dutch Partridge Dog (or "Drent" for Drenthe) in English, approximately 5,000 dogs are registered with the breed club in the Netherlands, and breed clubs operate in Belgium, Denmark, Scandinavia and North America.  The Drentsche Patrijshond bears some resemblance to both spaniel and setter types of dog.  An excellent pointer and retriever, this dog is often used to hunt fowl and adapts equally well to the field or marshes.

Breed standard (dogs): A breed standard (also called bench standard or the standard) in the dog fancy is a set of guidelines covering specific "externally observable" qualities such as "appearance", "movement", and "temperament" for that dog breed.  Breed standards are not scientific documents, but are written for each breed by clubs of hobbyists called breed clubs for their own specific requirements.  Details and definitions within breed standards for a specific dog breed may vary from breed club to breed club and from country to country.  Dog breed standards are similar in form and function to breed standards for other domesticated animals.

Question: Which dog breed, Drentse Patrijshond or Ratonero Murciano de Huerta, is a Spanish breed of dog originating from Murcia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_breed_name": {
      "type": "string",
      "description": "The name of the dog breed that matches the specified criteria."
    },
    "breed_origin_country": {
      "type": "string",
      "description": "The country of origin for the identified breed."
    },
    "breed_origin_region": {
      "type": "string",
      "description": "The specific region or province of origin for the identified breed."
    },
    "is_spanish_breed": {
      "type": "boolean",
      "description": "True if the identified breed is Spanish."
    },
    "originates_from_murcia": {
      "type": "boolean",
      "description": "True if the identified breed originates from Murcia."
    }
  },
  "required": [
    "identified_breed_name",
    "breed_origin_country",
    "breed_origin_region",
    "is_spanish_breed",
    "originates_from_murcia"
  ],
  "additionalProperties": false
}
