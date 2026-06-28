 # Tech-Spec.md

## Stack
- Language: TypeScript for a robust and scalable solution, with a focus on Type Safety.
- Framework: Express.js for building the API and handling HTTP requests.
- Runtime: Node.js for running the server-side code.

## Hosting
- Free-Tier-First: AWS Amplify for hosting the application in a free tier initially, with the potential for scaling to paid tiers as usage increases.
- Specific Platforms: Windows and Linux for supporting the primary operating systems used by PC gamers.

## Data Model
- Tables/Collections:
  - `Games`: Game titles, IDs, and supported platforms.
  - `Users`: User accounts, including username, password (hashed and salted), and API key.
  - `Sessions`: Session data, including session ID, user ID, game ID, start time, and end time.
  - `CrashReports`: Crash reports, including session ID, timestamp, error message, and system details.
- Key Fields:
  - `id`: Unique identifier for each record.
  - `username`: Username for user accounts.
  - `api_key`: API key for user authentication.
  - `game_id`: Unique identifier for each game.
  - `session_id`: Unique identifier for each session.

## API Surface
- `GET /api/games`: Retrieve a list of supported games.
- `POST /api/auth/register`: Register a new user account.
- `POST /api/auth/login`: Authenticate a user and return an API key.
- `POST /api/sessions/start`: Start a new gaming session, associating it with the authenticated user.
- `POST /api/sessions/end`: End an existing gaming session.
- `POST /api/crash-reports`: Submit a crash report for analysis.
- `GET /api/crash-reports`: Retrieve a list of crash reports for the authenticated user.
- `GET /api/crash-reports/:id`: Retrieve a specific crash report by ID.

## Security Model
- Auth: JWT-based authentication for securing API endpoints.
- Secrets: Environment variables for storing sensitive information, such as database credentials and API keys.
- IAM: AWS IAM policies for managing access to AWS resources.

## Observability
- Logs: Logging framework (such as Winston.js) for capturing and analyzing application logs.
- Metrics: Prometheus for monitoring application performance and resource usage.
- Traces: Jaeger for distributed tracing and debugging.

## Build/CI
- Build: Webpack for bundling the application code and assets.
- CI: GitHub Actions for automating the build, test, and deployment process.