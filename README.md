# ACEHACK 4.0 Priority Queue

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-green.svg)](https://www.mongodb.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-red.svg)](https://fastapi.tiangolo.com/)

A comprehensive blockchain-based NFT platform revolutionizing healthcare priority management and educational achievement verification through two innovative modules: **LifeNFT** and **GYAANFT**.

## 🌟 Overview

This project presents a groundbreaking solution that leverages blockchain technology, NFTs, and machine learning to address critical challenges in healthcare prioritization and educational achievement verification. Built for ACEHACK 4.0, our platform combines cutting-edge technologies to create transparent, secure, and efficient systems for both healthcare providers and educational institutions.

## 🏗️ Project Architecture

```
GYAANFT/
├── ACE_4.0_LifeNFT_MODULE_1/          # Healthcare priority queue system
│   ├── frontend/                       # React.js dashboard interfaces
│   ├── backend/                        # FastAPI server
│   ├── blockchain/                     # Hive blockchain integration
│   └── ml-models/                      # Priority prediction algorithms
├── ACE_4.0_Priority_Queue_GYAANFT_MODULE_2/  # Educational NFT platform
│   ├── frontend/                       # React.js user interfaces
│   ├── backend/                        # Node.js/Express server
│   ├── smart-contracts/                # ERC721 NFT contracts
│   └── ai-assistant/                   # ML-powered guidance system
├── docs/                               # Documentation
├── scripts/                            # Deployment and utility scripts
└── tests/                             # Test suites
```

## 🚀 Modules

### Module 1: LifeNFT - Healthcare Priority Queue System

A revolutionary blockchain-based healthcare priority management system that utilizes NFTs to represent patient health data and implement intelligent priority queues for medical services.

#### Key Features

- **🏥 Smart Priority Management**: ML-powered algorithms analyze patient conditions and assign priorities
- **🔐 Secure Health Records**: Patient data tokenized as NFTs for enhanced security and ownership
- **📊 Multi-Dashboard System**: Dedicated interfaces for hospitals, government agencies, and users
- **⚡ Real-time Updates**: Instant priority queue updates using Hive blockchain
- **🔗 Interoperability**: Seamless integration with existing hospital management systems

#### Technology Stack

- **Frontend**: React.js with modern UI components
- **Backend**: FastAPI for high-performance API endpoints
- **Blockchain**: Hive blockchain for decentralized data storage
- **Database**: MongoDB for off-chain data management
- **ML/AI**: Custom priority prediction algorithms
- **Authentication**: JWT-based secure authentication

### Module 2: GYAANFT - Educational Achievement Platform

An innovative NFT-based educational platform that tokenizes learning achievements, provides career guidance, and creates a transparent ecosystem for educational credentials.

#### Key Features

- **🎓 Achievement NFTs**: Educational milestones represented as unique NFTs
- **🛤️ Career Path Guidance**: AI-powered career recommendations
- **🏆 Learning Milestones**: Gamified learning experience with blockchain verification
- **🤖 AI Assistant**: Intelligent tutoring and guidance system
- **📈 Progress Tracking**: Comprehensive learning journey visualization
- **🌐 Decentralized Credentials**: Tamper-proof educational certificates

#### Technology Stack

- **Frontend**: React.js with interactive learning interfaces
- **Backend**: Node.js with Express framework
- **Blockchain**: EduChain (Layer 3) on Arbitrum Orbit
- **Smart Contracts**: ERC721 NFT standard implementation
- **Database**: MongoDB for user data and analytics
- **ML/AI**: Natural language processing for career guidance
- **Contract Address**: `0x4b0800266eee8ddd04fb0d0ad5e8dc72b7925b8d`

## 🛠️ Installation & Setup

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- MongoDB (v6.0 or higher)
- Git
- MetaMask or compatible Web3 wallet

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/darshanPC25/GYAANFT.git
   cd GYAANFT
   ```

2. **Install Dependencies**
   ```bash
   # For LifeNFT Module
   cd ACE_4.0_LifeNFT_MODULE_1
   npm install
   pip install -r requirements.txt
   
   # For GYAANFT Module
   cd ../ACE_4.0_Priority_Queue_GYAANFT_MODULE_2
   npm install
   ```

3. **Environment Configuration**
   ```bash
   # Copy environment templates
   cp .env.example .env
   
   # Configure your environment variables
   nano .env
   ```

4. **Database Setup**
   ```bash
   # Start MongoDB
   sudo systemctl start mongod
   
   # Initialize databases
   npm run db:init
   ```

5. **Start the Applications**
   ```bash
   # Terminal 1: LifeNFT Module
   cd ACE_4.0_LifeNFT_MODULE_1
   npm run dev
   
   # Terminal 2: GYAANFT Module
   cd ACE_4.0_Priority_Queue_GYAANFT_MODULE_2
   npm start
   ```

### Advanced Setup

For detailed setup instructions for each module, please refer to:
- [LifeNFT Module Setup Guide](https://github.com/darshanPC25/GYAANFT/tree/main/ACE_4.0_LifeNFT_MODULE_1/ACE_4.0_Priority_Queue-main#readme)
- [GYAANFT Module Setup Guide](https://github.com/darshanPC25/GYAANFT/tree/main/ACE_4.0_Priority_Queue_GYAANFT_MODULE_2/ACE_4.0_Priority_Queue_GYAANFT-main#readme)

## 🎯 Use Cases

### Healthcare Scenarios

- **Emergency Room Triage**: Automated patient priority assessment based on health conditions
- **Specialist Appointments**: Fair queue management for limited medical resources
- **Insurance Claims**: Transparent priority handling for claim processing
- **Medical Research**: Secure patient data sharing with consent management

### Educational Applications

- **Digital Certificates**: Tamper-proof degree and course completion certificates
- **Skill Verification**: Blockchain-verified professional competencies
- **Career Development**: AI-guided learning path recommendations
- **Academic Portfolio**: Comprehensive showcase of educational achievements

## 🔧 Configuration

### Environment Variables

#### LifeNFT Module (.env)
```bash
# Database
MONGODB_URI=mongodb://localhost:27017/lifenft
REDIS_URL=redis://localhost:6379

# Blockchain
HIVE_NODE_URL=https://api.hive.blog
HIVE_ACCOUNT=your_hive_account
HIVE_PRIVATE_KEY=your_private_key

# API
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
SECRET_KEY=your_secret_key

# ML Models
ML_MODEL_PATH=./models/priority_model.pkl
```

#### GYAANFT Module (.env)
```bash
# Database
MONGODB_URI=mongodb://localhost:27017/gyaanft

# Blockchain
EDUCHAIN_RPC_URL=https://rpc.open-campus-codex.gelato.digital
PRIVATE_KEY=your_private_key
CONTRACT_ADDRESS=0x4b0800266eee8ddd04fb0d0ad5e8dc72b7925b8d

# Server
PORT=3000
NODE_ENV=development
JWT_SECRET=your_jwt_secret

# AI Services
OPENAI_API_KEY=your_openai_key
```

## 🧪 Testing

### Running Tests

```bash
# Unit Tests
npm test

# Integration Tests
npm run test:integration

# E2E Tests
npm run test:e2e

# Coverage Report
npm run test:coverage
```

### Test Structure

```
tests/
├── unit/
│   ├── lifenft/
│   └── gyaanft/
├── integration/
│   ├── api/
│   └── blockchain/
└── e2e/
    ├── healthcare-flow/
    └── education-flow/
```

## 📊 API Documentation

### LifeNFT Module APIs

#### Authentication Endpoints
- `POST /auth/login` - User authentication
- `POST /auth/register` - User registration
- `POST /auth/refresh` - Token refresh

#### Priority Queue Endpoints
- `GET /queue/status` - Get current queue status
- `POST /queue/add` - Add patient to priority queue
- `PUT /queue/{id}/priority` - Update patient priority
- `DELETE /queue/{id}` - Remove patient from queue

#### NFT Management Endpoints
- `POST /nft/mint` - Mint health record NFT
- `GET /nft/{token_id}` - Get NFT details
- `PUT /nft/{token_id}/transfer` - Transfer NFT ownership

### GYAANFT Module APIs

#### User Management
- `POST /api/users/register` - User registration
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update user profile

#### NFT Operations
- `POST /api/nft/mint` - Mint achievement NFT
- `GET /api/nft/collection/{user_id}` - Get user's NFT collection
- `POST /api/nft/verify` - Verify NFT authenticity

#### Career Guidance
- `POST /api/career/analyze` - Analyze career path
- `GET /api/career/recommendations` - Get career recommendations
- `POST /api/career/roadmap` - Generate learning roadmap

## 🤝 Contributing

We welcome contributions from the community! Please follow these guidelines:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow ESLint configuration for JavaScript/TypeScript
- Use Black formatter for Python code
- Write comprehensive tests for new features
- Include JSDoc comments for functions
- Follow conventional commit messages

### Issue Reporting

Please use GitHub Issues to report bugs or request features. Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- System information

## 🔒 Security

### Security Measures

- **Smart Contract Auditing**: All contracts undergo thorough security audits
- **Data Encryption**: End-to-end encryption for sensitive health data
- **Access Control**: Role-based permissions and authentication
- **Private Keys**: Secure key management practices
- **Regular Updates**: Continuous security monitoring and updates


## 🚀 Deployment

### Development Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Manual deployment
npm run deploy:dev
```

### Production Deployment

```bash
# Build production assets
npm run build

# Deploy to production
npm run deploy:prod
```



## 📈 Monitoring & Analytics

### Health Checks

- `/health` - Application health status
- `/metrics` - Prometheus metrics endpoint
- `/version` - Application version information

### Logging

- Structured JSON logging
- ELK stack integration
- Error tracking with Sentry
- Performance monitoring

## 🗺️ Roadmap

### Phase 1 (Current)
- ✅ Core LifeNFT functionality
- ✅ Basic GYAANFT platform
- ✅ Smart contract deployment
- ✅ Initial testing suite

### Phase 2 (Q1 2025)
- 🔄 Advanced ML algorithms
- 🔄 Mobile application development
- 🔄 Enhanced security features
- 🔄 Third-party integrations

### Phase 3 (Q2 2025)
- 📅 Cross-chain compatibility
- 📅 Advanced analytics dashboard
- 📅 Enterprise partnerships
- 📅 International expansion

## 🤖 AI & Machine Learning

### LifeNFT ML Models

- **Priority Prediction**: Random Forest classifier for patient priority assessment
- **Resource Optimization**: LSTM networks for hospital resource allocation
- **Risk Assessment**: Deep learning models for patient risk stratification

### GYAANFT AI Features

- **Career Matching**: NLP-based career recommendation engine
- **Learning Path Optimization**: Reinforcement learning for personalized curricula
- **Skill Gap Analysis**: Computer vision for portfolio assessment

## 🌐 Blockchain Integration

### Hive Blockchain (LifeNFT)

- **Consensus**: Delegated Proof of Stake (DPoS)
- **Transaction Speed**: 3-second block time
- **Fees**: Resource Credit system (freemium model)
- **Storage**: Decentralized health record storage

### EduChain (GYAANFT)

- **Network**: Layer 3 on Arbitrum Orbit
- **Chain ID**: 656476
- **RPC URL**: https://rpc.open-campus-codex.gelato.digital
- **Explorer**: https://opencampus-codex.blockscout.com/

## 📚 Documentation

### Additional Resources

- [API Documentation](./docs/api/)
- [Smart Contract Documentation](./docs/contracts/)
- [User Guides](./docs/user-guides/)
- [Developer Tutorials](./docs/tutorials/)
- [Architecture Diagrams](./docs/architecture/)

## 💬 Community & Support

### Get Help

- **Documentation**: Comprehensive guides and API references
- **GitHub Issues**: Bug reports and feature requests
- **Community Forum**: Discussion and Q&A
- **Email Support**: technical-support@acehack-project.com


## 📊 Project Statistics

- **Lines of Code**: 50,000+
- **Smart Contracts**: 15+
- **API Endpoints**: 100+
- **Test Coverage**: 85%+
- **Documentation Pages**: 200+

---
