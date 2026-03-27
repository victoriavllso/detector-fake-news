package com.detector.backend.config

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.http.HttpMethod
import org.springframework.security.config.annotation.web.builders.HttpSecurity
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.security.web.SecurityFilterChain
import org.springframework.web.cors.CorsConfiguration
import org.springframework.web.cors.UrlBasedCorsConfigurationSource

@Configuration
@EnableWebSecurity // Adicionado para garantir a aplicação da config
class SecurityConfig {

    @Bean
    fun passwordEncoder(): PasswordEncoder = BCryptPasswordEncoder()

    @Bean
    fun corsConfigurationSource(): UrlBasedCorsConfigurationSource {
        val config = CorsConfiguration()
        config.allowCredentials = true
        config.allowedOrigins = listOf("http://localhost:3000") // Apenas a origem exata do front
        config.allowedHeaders = listOf("*")
        config.allowedMethods = listOf("OPTIONS", "GET", "POST", "PUT", "DELETE")
        // Remova allowedOriginPatterns = listOf("*") para evitar conflito com allowCredentials = true

        val source = UrlBasedCorsConfigurationSource()
        source.registerCorsConfiguration("/**", config)
        return source
    }

    @Bean
    fun filterChain(http: HttpSecurity): SecurityFilterChain {
        http
            .cors { } // O Spring Security vai usar automaticamente o Bean "corsConfigurationSource"
            .csrf { it.disable() }
            .authorizeHttpRequests { auth ->
                auth.requestMatchers(HttpMethod.OPTIONS, "/**").permitAll()
                auth.requestMatchers("/api/auth/**", "/predict").permitAll()
                auth.anyRequest().authenticated()
            }
            .httpBasic { it.disable() }
            .formLogin { it.disable() }

        return http.build()
    }
}