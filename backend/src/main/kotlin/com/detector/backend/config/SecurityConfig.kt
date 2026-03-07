package com.detector.backend.config

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.security.config.annotation.web.builders.HttpSecurity
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.security.web.SecurityFilterChain

@Configuration
class SecurityConfig {

    @Bean
    fun passwordEncoder(): PasswordEncoder = BCryptPasswordEncoder()

    @Bean
    fun filterChain(http: HttpSecurity): SecurityFilterChain {
        http
            .csrf { it.disable() } // Desabilitado para facilitar testes iniciais via Postman/Insomnia
            .authorizeHttpRequests { auth ->
                auth.requestMatchers("/api/auth/**").permitAll() // Endpoints de login/registro
                auth.anyRequest().authenticated()
            }
            .httpBasic { } // Permite autenticação básica via Header (p/ testar sem front)
            .formLogin { } // Habilita a página de login padrão do Spring no navegador
            
        return http.build()
    }
}