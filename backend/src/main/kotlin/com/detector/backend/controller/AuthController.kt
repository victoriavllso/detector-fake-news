package com.detector.backend.controller

import com.detector.backend.entity.User
import com.detector.backend.dto.RegisterRequest
import com.detector.backend.repository.UserRepository
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import jakarta.validation.Valid

@RestController
@RequestMapping("/api/auth")
class AuthController(
    private val userRepository: UserRepository,
    private val passwordEncoder: PasswordEncoder
) {
    @PostMapping("/register")
    fun register(@RequestBody @Valid request: RegisterRequest): String {
        val username = requireNotNull(request.username)
        val password = requireNotNull(request.password)
        val encodedPassword: String = passwordEncoder.encode(password)!!

        val encodedUser = User(
            usernameField = username,
            passwordField = encodedPassword
        )
        userRepository.save(encodedUser)
        return "Usuário registrado com sucesso!"
    }
}