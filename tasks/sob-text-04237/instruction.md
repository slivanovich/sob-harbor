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
Erythrina americana: Erythrina America, (coral tree or colorines), is a flowering plant of the genus "Erythrina" which is native to Mexico.  Colorín (plural colorines) is the name of a type of tree, "Erythrina americana" also called Tzompāmitl.  The word colorín means color chillón—a “gaudy” or “loud” color (Williams 1959).

Caatinga: Caatinga (] ) is a type of desert vegetation, which can also be called Jola Jolilo (Jou-lah-Jouh-Liloy).  It is the indian name for the Caatinga, and an ecoregion characterized by this vegetation in interior northeastern Brazil.  The name "Caatinga" is a Tupi word meaning "white forest" or "white vegetation" ("caa" = forest, vegetation, "tinga" = white).

Desert riparian: Desert riparian is a North American desert vegetation type (or biome) occurring in the bottoms of canyons and drainages that have water at or near the surface most of the year.  It is contrasted with the desert dry wash vegetation type in which water at or near the surface is lacking most of the year.  The visual character is of large, lush green trees surrounded by dry desert vegetation and soil coloration.  The area may be in a patch surrounding a spring (oasis), or in a strand following the course of water flow.  Over 80% of known desert wildlife species use desert riparian areas.  Common dominant species include Fremont cottonwood ("Populus fremontii"), Arizona ash ("Fraxinus velutina"), arroyo willow ("Salix lasiolepis"), Goodding's willow ("Salix gooddingii"), red willow ("Salix laevigata"), California fan palm ("Washingtonia filifera"), and invasive species such as salt cedar ("Tamarix ramosissima"), giant reed ("Arundo donax"), and Russian olive ("Elaeagnus angustifolia").  Salt cedar is particularly causing problems for this ecosystem because it is able to extract water more efficiently than cottonwoods and willows.  Many noninvasive non-native species may also be found because springs and surface water areas in the desert often were old homesites where such species were intentionally planted, such as elm, black locust, and assorted fruit trees.

Vegetation and slope stability: Vegetation and slope stability are interrelated by the ability of the plant life growing on slopes to both promote and hinder the stability of the slope.  The relationship is a complex combination of the type of soil, the rainfall regime, the plant species present, the slope aspect, and the steepness of the slope.  Knowledge of the underlying slope stability as a function of the soil type, its age, horizon development, compaction, and other impacts is a major underlying aspect of understanding how vegetation can alter the stability of the slope.  There are four major ways in which vegetation influences slope stability: wind throwing, the removal of water, mass of vegetation (surcharge), and mechanical reinforcement of roots.

Erythrina falcata: Erythrina falcata (syn.  "Corallodendron falcatum" (Benth.)  Kuntze, "Erythrina crista-galli" L. var.  "inermis" Speg., "Erythrina martii" Colla), commonly known as the Brazilian coral tree, is a timber tree native to Atlantic Forest vegetation in Brazil, Paraguay and Argentina.  This plant is also used as a medicinal plant and ornamental plant which is attractive to birds.

Wildfire: A wildfire or wildland fire is a fire in an area of combustible vegetation that occurs in the countryside or rural area.  Depending on the type of vegetation where it occurs, a wildfire can also be classified more specifically as a brush fire, bush fire, desert fire, forest fire, grass fire, hill fire, peat fire, vegetation fire, or veld fire.  Fossil charcoal indicates that wildfires began soon after the appearance of terrestrial plants 420 million years ago.  Wildfire’s occurrence throughout the history of terrestrial life invites conjecture that fire must have had pronounced evolutionary effects on most ecosystems' flora and fauna.  Earth is an intrinsically flammable planet owing to its cover of carbon-rich vegetation, seasonally dry climates, atmospheric oxygen, and widespread lightning and volcano ignitions.

Vegetation classification: Vegetation classification is the process of classifying and mapping the vegetation over an area of the earth's surface.  Vegetation classification is often performed by state based agencies as part of land use, resource and environmental management.  Many different methods of vegetation classification have been used.  In general, there has been a shift from structural classification used by forestry for the mapping of timber resources, to floristic community mapping for biodiversity management.  Whereas older forestry-based schemes considered factors such as height, species and density of the woody canopy, floristic community mapping shifts the emphasis onto ecological factors such as climate, soil type and floristic associations.  Classification mapping is usually now done using Geographic Information Systems (GIS) software.

Lythrum: Lythrum is a genus of 38 species of flowering plants native to the temperate world.  Commonly known as loosestrife (a name they share with "Lysimachia", which are not closely related).  They are among 32 genera of the family Lythraceae.

Erythrina: Erythrina is a genus of flowering plants in the pea family, Fabaceae.  It contains about 130 species, which are distributed in tropical and subtropical regions worldwide.  They are trees, growing up to 30 m in height.  The generic name is derived from the Greek word ερυθρóς ("erythros"), meaning "red," referring to the flower color of certain species.

Erythrina fusca: Erythrina fusca is a species of flowering tree in the legume family, Fabaceae.  It is known by many common names, including purple coraltree, gallito, bois immortelle, bucayo, and the more ambiguous "bucare" and "coral bean".  "E. fusca" has the widest distribution of any "Erythrina" species; it is the only one found in both the New and Old World.  It grows on coasts and along rivers in tropical Asia, Oceania, the Mascarene Islands, Madagascar, Africa, and the Neotropics.

Question: What type of vegetation does Lythrum and Erythrina have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_vegetation_type": {
      "type": "string",
      "description": "The type of vegetation that Lythrum and Erythrina have in common."
    },
    "genera_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genera for which the common vegetation type is identified."
    },
    "description_sources": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "vegetation_description": {
            "type": "string",
            "description": "The description of the vegetation type for this genus from the context."
          }
        },
        "required": [
          "genus_name",
          "vegetation_description"
        ],
        "additionalProperties": false
      },
      "description": "Details from the context describing the vegetation for each genus."
    }
  },
  "required": [
    "common_vegetation_type",
    "genera_involved",
    "description_sources"
  ],
  "additionalProperties": false
}
