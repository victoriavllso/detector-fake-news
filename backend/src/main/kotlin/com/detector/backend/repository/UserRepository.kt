package com.detector.backend.repository

import com.detector.backend.entity.User
import org.springframework.data.jpa.repository.JpaRepository
import org.springframework.stereotype.Repository

@Repository
interface UserRepository : JpaRepository<User, Long> { // entidate JPA é o User
    fun findByUsername(username: String): User?
}