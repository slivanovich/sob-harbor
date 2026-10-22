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
Nipponanthemum: Nipponanthemum nipponicum, common names "Nippon daisy" or "Montauk daisy," is a plant species native to coastal regions of Japan but cultivated as an ornamental in other regions.  It is now naturalized as an escape along seashores in New York and New Jersey.  It is the only species in the genus Nipponanthemum, formerly considered part of "Chrysanthemum".

List of theatre festivals: Theatre festivals are amongst the earliest types of festival.  Classical Greek theatre was associated with religious festivals dedicated to Dionysus, called the City Dionysia.  The medieval mystery plays were presented at the major Christian feasts.  Theatre as an everyday part of life is a comparatively recent phenomenon.

Dionysia (plant): Dionysia is a genus containing 49 species of flowering plants in the family Primulaceae.  They are small, cushion-forming alpines native to mountains in central Asia.  They are usually evergreen perennials with felted leaves, covered with bright yellow or pink, five-petalled flowers in spring.  They are often difficult to cultivate if the correct conditions are not provided.

Entity–relationship model: An entity–relationship model (ER model) describes inter-related things of interest in a specific domain of knowledge.  An ER model is composed of entity types (which classify the things of interest) and specifies relationships that can exist between instances of those entity types.

Blittable types: Blittable types are data types in . NET software applications which have a unique characteristic.  Data is often represented in memory differently in managed and unmanaged code in the Microsoft . NET framework.  However, blittable types are defined as having an identical presentation in memory for both environments, and can be directly shared.  Understanding the difference between blittable and non-blittable types can aid in using COM Interop or P/Invoke, two techniques for interoperability in . NET applications.

Declaration (computer programming): In computer programming, a declaration is a language construct that specifies properties of an identifier: it declares what a word (identifier) "means:."  Declarations are most commonly used for functions, variables, constants, and classes, but can also be used for other entities such as enumerations and type definitions.  Beyond the name (the identifier itself) and the kind of entity (function, variable, etc.), declarations typically specify the data type (for variables and constants), or the type signature (for functions); types may also include dimensions, such as for arrays.  A declaration is used to announce the existence of the entity to the compiler; this is important in those strongly typed languages that require functions, variables, and constants, and their types to be specified with a declaration before use, and is used in forward declaration.  The term "declaration" is frequently contrasted with the term "definition", but meaning and usage varies significantly between languages; see below.

U.S. state: A U.S. state is a constituent political entity of the United States of America.  There are currently 50 states, which are bound together in a union with each other.  Each state holds governmental jurisdiction over a defined geographic territory, and shares its sovereignty with the United States federal government.  Due to the shared sovereignty between each state and the federal government, Americans are citizens of both the federal republic and of the state in which they reside.  State citizenship and residency are flexible, and no government approval is required to move between states, except for persons covered by certain types of court orders (e.g., paroled convicts and children of divorced spouses who are sharing custody).

List of business entities: A business entity is an entity that is formed and administered as per corporate law in order to engage in business activities, charitable work, or other activities allowable.  Most often, business entities are formed to sell a product or a service.  There are many types of business entities defined in the legal systems of various countries.  These include corporations, cooperatives, partnerships, sole traders, limited liability company and other specifically permitted and labelled types of entities.  The specific rules vary by country and by state or province.  Some of these types are listed below, by country.  For guidance, approximate equivalents in the company law of English-speaking countries are given in most cases,

SGML entity: In the Standard Generalized Markup Language (SGML), an entity is a primitive data type, which associates a string with either a unique alias (such as a user-specified name) or an SGML reserved word (such as codice_1).  Entities are foundational to the organizational structure and definition of SGML documents.  The SGML specification defines numerous entity types, which are distinguished by keyword qualifiers and context.  An entity string value may variously consist of plain text, SGML tags, and/or references to previously-defined entities.  Certain entity types may also invoke external documents.  Entities are called by reference.

Shared services center: A shared services center – a center for shared services in an organization – is the entity responsible for the execution and the handling of specific operational tasks, such as accounting, human resources, payroll, IT, legal, compliance, purchasing, security.  The shared services center is often a spin-off of the corporate services to separate all operational type of tasks from the corporate headquarters, which has to focus on a leadership and corporate governance type of role.  As shared services centers are often cost centers, they are quite cost-sensitive also in terms of their headcount, labour costs and location selection criteria.

Question: Nipponanthemum and Dionysia, are types of which shared entity?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shared_entity_type": {
      "type": "string",
      "description": "The common category or type that the given entities belong to."
    },
    "entities_provided": {
      "type": "array",
      "description": "A list of the specific entities mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "contextual_evidence": {
      "type": "string",
      "description": "A summary of the evidence from the context supporting the shared entity type."
    }
  },
  "required": [
    "shared_entity_type",
    "entities_provided",
    "contextual_evidence"
  ],
  "additionalProperties": false
}
