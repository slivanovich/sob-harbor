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
FCI Retriever, Flushing Dog and Water Dog Group: The Retriever, Flushing Dog and Water Dog Group is a designation used only by the Fédération Cynologique Internationale for a group of dog breeds consisting of Retrievers, Flushing Dogs and Water Dogs.

Tweed Water Spaniel: The Tweed Water Spaniel, or Tweed Spaniel, is a breed of dog extinct since the 19th century.  It is best known for being involved in the early development of the modern Curly Coated Retriever and Golden Retriever breeds of dogs.  They were described as a generally brown athletic dogs from the area around Berwick-upon-Tweed near the River Tweed and close to the Scottish Borders.  A type of water dog, the breed was not well known outside the local area.  This breed may have been created by crossing local water dogs with imported St. John's water dog, another breed which is also now extinct.

Whippet: The Whippet (also English Whippet or Snap dog) is a dog breed of medium-size.  They are a sighthound breed that originated in England, where they descended from greyhounds. Whippets today still strongly resemble a smaller greyhound.  Shown in the Hound group, Whippets have relatively few health problems other than arrhythmia.  Whippets also participate in dog sports such as lure coursing, agility, and flyball.  The name is derived from an early 17th-century word, now obsolete, meaning to "move briskly".

Grief therapy dog: A grief therapy dog (also known as an emotional support dog, companion dog, or comfort dog) is a form of animal-assisted therapy.  Dogs have been proven to be able to assist people in overcoming grief, which has led to a recent rise in the use of therapy dogs; although animal-assisted therapy theory has been around since World War II.  Grief therapy dogs can be found in locations such as funeral homes, hospitals, nursing homes, schools, and hospices, and may provide support in situations such as funeral services, counseling sessions, and disaster relief.  Popular breeds used as therapy dogs include the Portuguese Water Dog, Bernese Mountain Dog, St. Bernard, and Golden Retriever.

Moscow Water Dog: The Moscow Water Dog, also known as the Moscow Diver, Moscow Retriever or Moskovsky Vodolaz, is a little-known dog breed derived from the Newfoundland, Caucasian Shepherd Dog and East European Shepherd.  It is now extinct, but was used in the development of the  Black Russian Terrier.  The Moscow Water Dog was produced only by the Red Star Kennels, the state operated organization chartered to provide working dogs for the armed services.

Cantabrian Water Dog: The Cantabrian Water Dog (Spanish: perro de agua cantábrico ) is a landrace breed of dog developed in the coast of Cantabria, northern Spain, as an assistant to fishermen.  The breed was classified and recognized by the Breeds Committee of the Spanish Ministry of Environment on 22 March 2011.

Wetterhoun: The Wetterhoun (FCI No.221, translated into English as the Frisian Water Dog) is a breed of dog traditionally used as a hunting dog for hunting small mammals and waterfowl in the province of Fryslan in the Netherlands.  The name of the dog comes from the West Frisian "Wetterhûn" meaning "water dog."  Plural of Wetterhoun is Wetterhounen in Dutch.  The breed may also be called the "Otterhoun" (not to be confused with the Otterhound) or "Dutch Spaniel", although it is not a Spaniel-type dog.

Playa de Gulpiyuri: Playa de Gulpiyuri is a flooded sinkhole with an inland beach located near Llanes, Spain around 100 m from the Cantabrian Sea.  Roughly 40 meters in length, it is fully tidal due to a series of underground tunnels carved by the salt water of the Cantabrian Sea which allows water from the Bay of Biscay to create small waves.

Spanish Water Dog: The Spanish Water Dog (perro de agua español ) breed dates back several hundred years and has its origins most likely in Turkey from where it was imported into Spain as a general purpose sheepdog and guard.  It is also used sometimes as a gundog, and is skilled at retrieval from water.  The SWD has strong genetic links to other ancient water breeds such as the Portuguese Water Dog, the French Barbet and the Irish Water Spaniel.

Teddy Roosevelt Terrier: The Teddy Roosevelt Terrier is a small to medium-sized American hunting terrier.  Lower-set with shorter legs, more muscular, and heavier bone density than its cousin the American Rat Terrier.  There is much diversity in the history of the Teddy Roosevelt Terrier breed and it shares a common early history with the American Rat Terrier, Fox Paulistinha and Tenterfield Terrier.  It is said the Rat Terrier background stems from the terriers or other dogs that were brought over by early English and other working class immigrants.  Since the breed was a farm, hunting and utility dog there was little to no planned breeding other than breeding dogs with agreeable traits to each other in order to produce the desired work ethic in the dog.  It is assumed that the Feist (dog), Bull Terrier, Smooth Fox Terrier, Manchester Terrier, Whippet, Italian Greyhound, the now extinct English White Terrier, Turnspit dog and or Wry Legged Terrier all share in the Teddy Roosevelt Terrier's ancestry.  These early Ratting Terriers were then most likely bred to the Beagle or Beagle cross bred dogs (for increased scenting ability) and other dogs.  Maximizing the influences from these various breeds provides the modern Teddy Roosevelt Terrier with a keen sense of awareness and prey drive, an acute sense of smell and a very high intellect.  Although they tend to be aloof with strangers they are devoted companion dogs with a strong desire to please and be near their owners side at all times.

Question: Whippet and Cantabrian Water Dog, are breeds of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_category": {
      "type": "string",
      "description": "The common category that the mentioned breeds belong to."
    },
    "breeds_mentioned": {
      "type": "array",
      "description": "A list of the specific dog breeds mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "breed_count": {
      "type": "integer",
      "description": "The total number of breeds mentioned in the question."
    }
  },
  "required": [
    "common_category",
    "breeds_mentioned",
    "breed_count"
  ],
  "additionalProperties": false
}
