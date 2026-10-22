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
Stokes parameters: The Stokes parameters are a set of values that describe the polarization state of electromagnetic radiation.  They were defined by George Gabriel Stokes in 1852, as a mathematically convenient alternative to the more common description of incoherent or partially polarized radiation in terms of its total intensity ("I"), (fractional) degree of polarization ("p"), and the shape parameters of the polarization ellipse.  The effect of an optical system on the polarization of light can be determined by constructing the Stokes vector for the input light and applying Mueller calculus, to obtain the Stokes vector of the light leaving the system.

Stokes stream function: In fluid dynamics, the Stokes stream function is used to describe the streamlines and flow velocity in a three-dimensional incompressible flow with axisymmetry.  A surface with a constant value of the Stokes stream function encloses a streamtube, everywhere tangential to the flow velocity vectors.  Further, the volume flux within this streamtube is constant, and all the streamlines of the flow are located on this surface.  The velocity field associated with the Stokes stream function is solenoidal—it has zero divergence.  This stream function is named in honor of George Gabriel Stokes.

Navier–Stokes equations: In physics, the Navier–Stokes equations , named after Claude-Louis Navier and George Gabriel Stokes, describe the motion of viscous fluid substances.  These balance equations arise from applying Newton's second law to fluid motion, together with the assumption that the stress in the fluid is the sum of a diffusing viscous term (proportional to the gradient of velocity) and a pressure term—hence describing "viscous flow".  The main difference between them and the simpler Euler equations for inviscid flow is that Navier–Stokes equations also factor in the Froude limit (no external field) and are not conservation equations, but rather a dissipative system, in the sense that they cannot be put into the quasilinear homogeneous form:

Strangers (The Walking Dead): "Strangers" is the second episode of the fifth season and 53rd episode overall of the post-apocalyptic horror television series "The Walking Dead", which aired on AMC on October 19, 2014.  The episode was written by series creator Robert Kirkman and directed by David Boyd.  In the episode, Rick Grimes (Andrew Lincoln)'s group encounters a priest, Father Gabriel Stokes (Seth Gilliam), who provides them solace in his church, while Rick contemplates Abraham Ford's (Michael Cudlitz) proposition to escort Dr. Eugene Porter (Josh McDermitt) to Washington, D.C. to cure the walker virus.

Stokes' law: In 1851, George Gabriel Stokes derived an expression, now known as Stokes' law, for the frictional force – also called drag force – exerted on spherical objects with very small Reynolds numbers in a viscous fluid.  Stokes' law is derived by solving the Stokes flow limit for small Reynolds numbers of the Navier–Stokes equations.

Stokes line: A Stokes line is the radiation of particular wavelengths present in the line spectra associated with fluorescence and the Raman scattering.  Stokes lines are of longer wavelength than that of the exciting radiation responsible for the fluorescence or Raman effect.  Stokes lines are named after Sir George Gabriel Stokes.

Gabriel Stokes (The Walking Dead): Father Gabriel Stokes is a fictional character from the comic book series "The Walking Dead" and is portrayed by Seth Gilliam in the television series of the same name.  He is an Episcopal priest from Georgia who has isolated himself from the outside world since the beginning of the outbreak, after shutting out the other members of his flock causing their deaths.  He is struggling to come to terms with the new reality he faces and his own faith.

Campbell–Stokes recorder: The Campbell–Stokes recorder (sometimes called a Stokes sphere) is a kind of sunshine recorder.  It was invented by John Francis Campbell in 1853 and modified in 1879 by Sir George Gabriel Stokes.  The original design by Campbell consisted of a glass sphere set into a wooden bowl with the sun burning a trace on the bowl.  Stokes's refinement was to make the housing out of metal and to have a card holder set behind the sphere.

Sir George Stokes, 1st Baronet: Sir George Gabriel Stokes, 1st Baronet, {'1': ", '2': ", '3': ", '4': "} ( ; 13 August 1819 – 1 February 1903), was a physicist and mathematician.  Born in Ireland, Stokes spent all of his career at the University of Cambridge, where he served as Lucasian Professor of Mathematics from 1849 until his death in 1903.  In physics, Stokes made seminal contributions to fluid dynamics (including the Navier–Stokes equations) and to physical optics.  In mathematics he formulated the first version of what is now known as Stokes' theorem and contributed to the theory of asymptotic expansions.  He served as secretary, then president, of the Royal Society of London.

Seth Gilliam: Seth Gilliam (born November 5, 1968) is an American actor.  He is best known for his portrayals of Ellis Carver on "The Wire", Clayton Hughes on "Oz", Dr. Alan Deaton on "Teen Wolf", and Father Gabriel Stokes on "The Walking Dead".

Question: The actor playing Father Gabriel Stokes was born when?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character portrayed by the actor."
    },
    "birth_date": {
      "type": "string",
      "description": "The full birth date of the actor."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actor."
    },
    "birth_month": {
      "type": "string",
      "description": "The birth month of the actor."
    },
    "birth_day": {
      "type": "integer",
      "description": "The birth day of the month for the actor."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "birth_date",
    "birth_year",
    "birth_month",
    "birth_day"
  ],
  "additionalProperties": false
}
