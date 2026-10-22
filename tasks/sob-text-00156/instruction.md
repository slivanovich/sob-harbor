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
Voronoi diagram: In mathematics, a Voronoi diagram is a partitioning of a plane into regions based on distance to points in a specific subset of the plane.  That set of points (called seeds, sites, or generators) is specified beforehand, and for each seed there is a corresponding region consisting of all points closer to that seed than to any other.  These regions are called Voronoi cells.  The Voronoi diagram of a set of points is dual to its Delaunay triangulation.

Zone diagram: A zone diagram is a certain geometric object which a variation on the notion of Voronoi diagram.  It was introduced by Tetsuo Asano, Jiri Matousek, and Takeshi Tokuyama in 2007.

Centroidal Voronoi tessellation: In geometry, a centroidal Voronoi tessellation (CVT) is a special type of Voronoi tessellation or Voronoi diagram.  A Voronoi tessellation is called centroidal when the generating point of each Voronoi cell is also its mean (center of mass).  It can be viewed as an optimal partition corresponding to an optimal distribution of generators.  A number of algorithms can be used to generate centroidal Voronoi tessellations, including Lloyd's algorithm for K-means clustering.

Voronoi formula: In mathematics, a Voronoi formula is an equality involving Fourier coefficients of automorphic forms, with the coefficients twisted by additive characters on either side.  It can be regarded as a Poisson summation formula for non-abelian groups.  The Voronoi (summation) formula for GL(2) has long been a standard tool for studying analytic properties of automorphic forms and their "L"-functions.  There have been numerous results coming out the Voronoi formula on GL(2).  The concept is named after Georgy Voronoy.

Georgy Voronoy: Georgy Feodosevich Voronoy (Ukrainian: Георгій Феодосійович Вороний ; Russian: Гео́ргий Феодо́сьевич Вороно́й ; 28 April 1868 – 20 November 1908) was a Russian and Ukrainian mathematician.  Among other things, he defined the Voronoi diagram.

Power diagram: In computational geometry, a power diagram is a partition of the Euclidean plane into polygonal cells defined from a set of circles, where the cell for a given circle "C" consists of all the points for which the power distance to "C" is smaller than the power distance to the other circles.  It is a form of generalized Voronoi diagram, and coincides with the Voronoi diagram of the circle centers in the case that all the circles have equal radii.

Voronoi pole: In geometry, the positive and negative Voronoi poles of a cell in a Voronoi diagram are certain vertices of the diagram.

Yuri Linnik: Yuri Vladimirovich Linnik (Russian: Ю́рий Влади́мирович Ли́нник ; January 8, 1915 – June 30, 1972) was a Soviet mathematician active in number theory, probability theory and mathematical statistics.

Fortune's algorithm: Fortune's algorithm is a sweep line algorithm for generating a Voronoi diagram from a set of points in a plane using O("n" log "n") time and O("n") space.  It was originally published by Steven Fortune in 1986 in his paper "A sweepline algorithm for Voronoi diagrams."

Weighted Voronoi diagram: In mathematics, a weighted Voronoi diagram in "n" dimensions is a special case of a Voronoi diagram.  The Voronoi cells in a weighted Voronoi diagram are defined in terms of a distance function.  The distance function may specify the usual Euclidean distance, or may be some other, special distance function.  Usually, the distance function is a function of the generator points' weights.

Question: Which of the following defined the Voronoi diagram: Georgy Voronoy or Yuri Linnik?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "concept_name": {
      "type": "string",
      "description": "The name of the mathematical concept in question."
    },
    "defined_by": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the person who defined the concept."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the person."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the person."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the person."
        }
      },
      "required": [
        "full_name",
        "nationality",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "other_person_considered": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the other person mentioned in the question."
        },
        "field_of_work": {
          "type": "string",
          "description": "The primary field of work for the other person."
        },
        "defined_concept": {
          "type": "boolean",
          "description": "Indicates if this person defined the concept in question."
        }
      },
      "required": [
        "full_name",
        "field_of_work",
        "defined_concept"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "concept_name",
    "defined_by",
    "other_person_considered"
  ],
  "additionalProperties": false
}
